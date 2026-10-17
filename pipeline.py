from agents import (
    build_search_agent,
    build_scrape_agent,
    writer_chain,
    critic_chain,
)


class ResearchCancelled(Exception):
    """Raised when the user asks ORBIT to stop between pipeline operations."""


def run_research_pipeline(topic: str, on_stage=None, cancel_event=None) -> dict:
    """Run the four research stages with cooperative cancellation checkpoints.

    Cancellation prevents any later stage from starting. A synchronous
    LangChain/network invocation already in progress cannot safely be killed
    from another Python thread, so Stop takes effect as soon as that call
    returns and the next checkpoint is reached.
    """
    state = {}

    def check_cancelled():
        if cancel_event is not None and cancel_event.is_set():
            raise ResearchCancelled("Research was stopped by the user.")

    def update_stage(stage: str, message: str):
        check_cancelled()
        if on_stage:
            on_stage(stage, message)

    # Stage 1: Search agent
    update_stage("search", "Searching the web for relevant sources...")
    search_agent = build_search_agent()
    check_cancelled()
    search_result = search_agent.invoke({
        "messages": [
            {"role": "user", "content": f"Conduct a web search on the topic: {topic}"}
        ]
    })
    check_cancelled()
    state["search_results"] = search_result["messages"][-1].content

    # Stage 2: Scraping agent
    update_stage("scrape", "Selecting a source and extracting deeper insights...")
    scrape_agent = build_scrape_agent()
    check_cancelled()
    scrape_result = scrape_agent.invoke({
        "messages": [
            (
                "user",
                f"Based on the following search results about '{topic}', "
                "pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}",
            )
        ]
    })
    check_cancelled()
    state["scraped_content"] = scrape_result["messages"][-1].content

    # Stage 3: Writer
    update_stage("write", "Synthesizing findings into a structured report...")
    combined_research = (
        f"Search Results:\n{state['search_results']}\n\n"
        f"Scraped Content:\n{state['scraped_content']}"
    )
    check_cancelled()
    write_result = writer_chain.invoke({"topic": topic, "research": combined_research})
    check_cancelled()
    state["report"] = write_result

    # Stage 4: Critic
    update_stage("critique", "Reviewing the report for gaps and quality...")
    check_cancelled()
    critique_result = critic_chain.invoke({"report": state["report"]})
    check_cancelled()
    state["critique"] = critique_result

    update_stage("complete", "Research report is ready.")
    return state
