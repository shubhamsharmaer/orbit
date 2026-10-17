"""Thread-safe background job manager for ORBIT's Streamlit UI."""
from __future__ import annotations

from copy import deepcopy
from threading import Event, Lock, Thread
from uuid import uuid4

from pipeline import ResearchCancelled, run_research_pipeline

_JOBS: dict[str, dict] = {}
_LOCK = Lock()


def _update(job_id: str, **updates) -> None:
    with _LOCK:
        job = _JOBS.get(job_id)
        if job is not None:
            job.update(updates)


def start_research_job(topic: str) -> str:
    job_id = uuid4().hex
    cancel_event = Event()
    job = {
        "job_id": job_id,
        "topic": topic,
        "status": "running",
        "current_stage": "search",
        "completed_stages": [],
        "message": "Starting research…",
        "result": None,
        "error": None,
        "cancel_event": cancel_event,
    }
    with _LOCK:
        _JOBS[job_id] = job

    def on_stage(stage: str, message: str) -> None:
        stage_order = ["search", "scrape", "write", "critique"]
        with _LOCK:
            current = _JOBS.get(job_id)
            if current is None:
                return
            completed = list(current["completed_stages"])
            if stage in stage_order:
                index = stage_order.index(stage)
                for previous in stage_order[:index]:
                    if previous not in completed:
                        completed.append(previous)
                current["current_stage"] = stage
            elif stage == "complete":
                completed = stage_order.copy()
                current["current_stage"] = None
            current["completed_stages"] = completed
            current["message"] = message

    def worker() -> None:
        try:
            result = run_research_pipeline(topic, on_stage=on_stage, cancel_event=cancel_event)
            if cancel_event.is_set():
                _update(job_id, status="cancelled", current_stage=None, message="Research stopped.")
            else:
                _update(job_id, status="completed", current_stage=None, result=result, message="Research complete.")
        except ResearchCancelled:
            _update(job_id, status="cancelled", current_stage=None, message="Research stopped.")
        except Exception as exc:
            _update(job_id, status="error", current_stage=None, error=f"{type(exc).__name__}: {exc}")

    Thread(target=worker, name=f"orbit-research-{job_id[:8]}", daemon=True).start()
    return job_id


def get_research_job(job_id: str | None) -> dict | None:
    if not job_id:
        return None
    with _LOCK:
        job = _JOBS.get(job_id)
        if job is None:
            return None
        # Keep the cancellation Event private to the manager.
        snapshot = {key: value for key, value in job.items() if key != "cancel_event"}
        return deepcopy(snapshot)


def request_stop(job_id: str) -> None:
    with _LOCK:
        job = _JOBS.get(job_id)
        if job is None or job["status"] != "running":
            return
        job["cancel_event"].set()
        job["status"] = "cancelled"
        job["current_stage"] = None
        job["message"] = "Research stopped."
