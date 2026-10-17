
import streamlit as st
from datetime import datetime


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ORBIT | Research Intelligence",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# CUSTOM STYLING — ORBIT DARK THEME
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    :root {
        --paper: #0b0f14;
        --surface: #111820;
        --surface-hover: #17212b;
        --report-bg: #10171e;
        --ink: #edf2eb;
        --muted: #929da8;
        --orange: #ff704f;
        --green: #c8f169;
        --line: #29343d;
    }

    /* ===== APP BACKGROUND ===== */

    .stApp {
        background:
            radial-gradient(
                ellipse at 82% 8%,
                rgba(67, 91, 63, 0.12),
                transparent 32%
            ),
            radial-gradient(
                ellipse at 5% 35%,
                rgba(255, 112, 79, 0.045),
                transparent 30%
            ),
            var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(11, 15, 20, 0.85);
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    /* ===== GLOBAL TEXT ===== */

    .stMarkdown,
    .stCaption,
    label,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: var(--ink);
    }

    .top-meta,
    .section-subtitle,
    .hero-copy,
    .agent-description {
        color: var(--muted);
    }

    /* ===== TOP NAVIGATION ===== */

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid var(--line);
        padding: 5px 0 20px;
        margin-bottom: 48px;
        gap: 16px;
    }

    .brand {
        color: var(--ink);
        font-size: 19px;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .brand-symbol {
        display: inline-flex;
        width: 30px;
        height: 30px;
        align-items: center;
        justify-content: center;
        border-radius: 9px;
        background: var(--orange);
        margin-right: 9px;
        color: #ffffff;
        font-size: 19px;
    }

    .top-meta {
        font: 11px 'DM Mono', monospace;
        letter-spacing: 1px;
        text-align: right;
    }

    /* ===== HERO SECTION ===== */

    .eyebrow {
        color: var(--orange);
        font: 11px 'DM Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 18px;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(42px, 6vw, 76px);
        line-height: 1.03;
        letter-spacing: -2.8px;
        margin: 0 0 20px;
        color: var(--ink);
    }

    .hero-title em {
        color: var(--green);
        font-weight: 500;
    }

    .hero-copy {
        font-size: 15px;
        line-height: 1.8;
        max-width: 490px;
        margin-bottom: 24px;
    }

    /* ===== ANIMATED ORBITAL PANEL ===== */

    .orbital-card {
        min-height: 255px;
        height: 100%;
        box-sizing: border-box;
        border-radius: 18px;
        padding: 25px;
        position: relative;
        overflow: hidden;
        background: radial-gradient(
            circle at center,
            #202d27 0%,
            #111b18 50%,
            #10151b 100%
        );
        border: 1px solid #29372f;
        box-shadow: inset 0 0 45px rgba(200, 241, 105, 0.025);
        color: var(--ink);
    }

    .orbital-card::before,
    .orbital-card::after {
        content: "";
        position: absolute;
        width: 170px;
        height: 170px;
        border: 1px solid rgba(200, 241, 105, 0.3);
        border-radius: 50%;
        top: 38px;
        left: 50%;
        transform: translateX(-50%);
        animation: hero-orbit 12s linear infinite;
    }

    .orbital-card::after {
        width: 225px;
        height: 225px;
        top: 10px;
        border-color: rgba(255, 98, 62, 0.45);
        animation-direction: reverse;
    }

    .orbit-core {
        position: absolute;
        left: 50%;
        top: 124px;
        transform: translate(-50%, -50%);
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: var(--green);
        color: #1b2a23;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        box-shadow: 0 0 40px rgba(200, 241, 105, 0.15);
        animation: pulse 3s ease-in-out infinite;
        z-index: 1;
    }

    .orbit-label {
        position: absolute;
        bottom: 23px;
        left: 25px;
        right: 25px;
        display: flex;
        justify-content: space-between;
        gap: 10px;
        font: 10px 'DM Mono', monospace;
        color: #b6c0b4;
        letter-spacing: 1px;
    }

    @keyframes hero-orbit {
        from { transform: translateX(-50%) rotate(0deg); }
        to { transform: translateX(-50%) rotate(360deg); }
    }

    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 0 20px #c8f16922;
        }
        50% {
            box-shadow: 0 0 45px #c8f16966;
        }
    }

    /* ===== SECTION HEADINGS ===== */

    .section-heading {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        font-weight: 700;
        margin: 38px 0 8px;
        color: var(--ink);
    }

    .section-number,
    .agent-index {
        color: var(--orange);
        font: 11px 'DM Mono', monospace;
    }

    .section-subtitle {
        font-size: 12px;
        margin-bottom: 18px;
    }

    /* ===== AGENT CARDS ===== */

    .agent-card {
        min-height: 125px;
        box-sizing: border-box;
        padding: 18px;
        border: 1px solid var(--line);
        border-radius: 14px;
        background: linear-gradient(
            145deg,
            rgba(26, 36, 45, 0.92),
            rgba(15, 22, 29, 0.92)
        );
        transition:
            border-color 0.25s,
            transform 0.25s,
            box-shadow 0.25s;
    }

    .agent-card:hover {
        transform: translateY(-4px);
        border-color: rgba(200, 241, 105, 0.55);
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.22);
    }

    .agent-name {
        color: var(--ink);
        font-size: 14px;
        font-weight: 700;
        margin: 10px 0 5px;
    }

    .agent-description {
        font-size: 11px;
        line-height: 1.6;
    }

    /* ===== RESEARCH INPUT ===== */

    .stTextInput input,
    .stTextArea textarea {
        background: var(--surface) !important;
        color: var(--ink) !important;
        border: 1px solid var(--line) !important;
        border-radius: 10px !important;
        padding: 13px !important;
        caret-color: var(--green);
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: var(--muted) !important;
        opacity: 1;
    }

    /* Keep the input clean on click: no browser/Streamlit focus ring. */
    .stTextInput input:focus,
    .stTextInput input:focus-visible,
    .stTextArea textarea:focus,
    .stTextArea textarea:focus-visible,
    [data-testid="stTextInput"] [data-baseweb="input"]:focus-within,
    [data-testid="stTextArea"] [data-baseweb="textarea"]:focus-within {
        outline: none !important;
        box-shadow: none !important;
        border-color: var(--line) !important;
    }

    /* Streamlit/BaseWeb may draw the ring on the input wrapper itself. */
    .stTextInput [data-baseweb="input"],
    .stTextArea [data-baseweb="textarea"] {
        outline: none !important;
        box-shadow: none !important;
    }

    .stTextInput [data-baseweb="input"]:focus-within,
    .stTextArea [data-baseweb="textarea"]:focus-within {
        outline: none !important;
        box-shadow: none !important;
        border-color: var(--line) !important;
    }

    [data-testid="stCaptionContainer"] {
        color: var(--muted);
    }

    /* ===== BUTTONS ===== */

    .stButton > button,
    .stFormSubmitButton > button,
    .stDownloadButton > button {
        min-height: 44px;
        border-radius: 10px;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .stFormSubmitButton > button[kind="primary"],
    .stButton > button[kind="primary"] {
        background: var(--orange);
        color: #ffffff;
        border: 1px solid var(--orange);
    }

    .stFormSubmitButton > button[kind="primary"]:hover,
    .stButton > button[kind="primary"]:hover {
        background: #e95131;
        border-color: #e95131;
        transform: translateY(-2px);
    }

    .stDownloadButton > button {
        background: var(--surface);
        color: var(--ink);
        border: 1px solid var(--line);
    }

    .stDownloadButton > button:hover {
        background: var(--surface-hover);
        border-color: var(--green);
        color: var(--green);
    }

    /* ===== REPORT WORKSPACE ===== */

    .report-header {
        background: linear-gradient(120deg, #17251f, #121c25);
        color: var(--ink);
        padding: 27px;
        border: 1px solid #2d4035;
        border-radius: 15px 15px 0 0;
        margin-top: 12px;
    }

    .report-kicker {
        color: var(--green);
        font: 10px 'DM Mono', monospace;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    .report-title {
        color: #f1f5ef;
        font: 29px 'Playfair Display', serif;
        line-height: 1.25;
        overflow-wrap: anywhere;
    }

    .report-body {
        border: 1px solid var(--line);
        border-top: 0;
        background: var(--report-bg);
        color: #dce4df;
        border-radius: 0 0 15px 15px;
        padding: 26px;
        line-height: 1.8;
    }

    /* The generated report should feel like an editorial dossier, not default Markdown. */
    .report-header {
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(ellipse at 92% 12%, rgba(200,241,105,.10), transparent 38%),
            linear-gradient(120deg, #17251f, #121c25 72%);
        box-shadow: 0 14px 38px rgba(0,0,0,.14);
    }

    .report-header::after {
        content: "ORBIT / INTELLIGENCE";
        position: absolute;
        right: 24px;
        bottom: 22px;
        color: rgba(237,242,235,.22);
        font: 9px 'DM Mono', monospace;
        letter-spacing: 2px;
    }

    .report-title {
        max-width: 850px;
        font-size: clamp(25px, 3vw, 36px);
        letter-spacing: -.7px;
    }

    .report-overline {
        margin: 0 0 12px;
        color: var(--muted);
        font: 10px 'DM Mono', monospace;
        letter-spacing: 1.6px;
        text-transform: uppercase;
    }

    .st-key-report-content {
        margin-top: 0;
        padding: clamp(20px, 3vw, 38px);
        border: 1px solid var(--line);
        border-top: 0;
        border-radius: 0 0 16px 16px;
        background: linear-gradient(180deg, rgba(16,23,30,.98), rgba(13,19,25,.98));
        box-shadow: 0 20px 55px rgba(0,0,0,.12);
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] {
        color: #d7e0dc;
        font-size: 14px;
        line-height: 1.85;
        overflow-wrap: anywhere;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] h1 {
        margin: 8px 0 22px;
        padding-bottom: 14px;
        border-bottom: 1px solid var(--line);
        color: var(--ink);
        font: 600 clamp(27px, 3vw, 36px)/1.2 'Playfair Display', serif;
        letter-spacing: -.5px;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] h2 {
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 34px 0 13px;
        padding: 0 0 10px;
        border-bottom: 1px solid rgba(41,52,61,.85);
        color: var(--ink);
        font: 600 23px/1.35 'Playfair Display', serif;
        letter-spacing: -.2px;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] h2::before {
        content: "";
        display: inline-block;
        flex: 0 0 4px;
        width: 4px;
        height: 22px;
        border-radius: 4px;
        background: var(--orange);
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] h3 {
        margin: 25px 0 8px;
        color: var(--green);
        font-size: 15px;
        font-weight: 700;
        letter-spacing: .1px;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] p {
        margin: 0 0 16px;
        color: #cbd5d2;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] strong {
        color: #f0f4ee;
        font-weight: 700;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] a {
        color: var(--green);
        text-decoration-color: rgba(200,241,105,.45);
        text-underline-offset: 3px;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] ul,
    .st-key-report-content [data-testid="stMarkdownContainer"] ol {
        margin: 8px 0 20px;
        padding-left: 25px;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] li {
        margin: 7px 0;
        padding-left: 4px;
        color: #cbd5d2;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] li::marker {
        color: var(--orange);
        font-weight: 700;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] blockquote {
        margin: 22px 0;
        padding: 15px 20px;
        border-left: 3px solid var(--green);
        border-radius: 0 10px 10px 0;
        background: rgba(200,241,105,.055);
        color: #dbe5d7;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] blockquote p {
        margin: 0;
        color: #dbe5d7;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 20px 0 26px;
        overflow: hidden;
        border: 1px solid var(--line);
        border-radius: 10px;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] thead tr {
        background: #1a262d;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] th {
        color: var(--green);
        font: 10px 'DM Mono', monospace;
        text-transform: uppercase;
        letter-spacing: .7px;
        border-bottom: 1px solid var(--line);
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] td,
    .st-key-report-content [data-testid="stMarkdownContainer"] th {
        padding: 12px 14px;
        text-align: left;
        border-right: 1px solid rgba(41,52,61,.7);
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] tr:nth-child(even) td {
        background: rgba(255,255,255,.018);
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] hr {
        border: 0;
        border-top: 1px solid var(--line);
        margin: 28px 0;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] :not(pre) > code {
        padding: 2px 6px;
        border: 1px solid #303c45;
        border-radius: 5px;
        background: #182129;
        color: var(--green);
        font: .9em 'DM Mono', monospace;
    }

    .st-key-report-content [data-testid="stMarkdownContainer"] pre {
        padding: 16px;
        border: 1px solid var(--line);
        border-radius: 10px;
        background: #090d11;
    }

    .report-actions-label {
        margin: 24px 0 10px;
        color: var(--muted);
        font: 10px 'DM Mono', monospace;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    /* Critic output gets its own designed review panel, matching the dossier. */
    .quality-review-card {
        margin-top: 30px;
        padding: 20px 24px 16px;
        border: 1px solid rgba(200,241,105,.24);
        border-bottom: 0;
        border-radius: 15px 15px 0 0;
        background:
            radial-gradient(ellipse at 95% 0%, rgba(200,241,105,.09), transparent 42%),
            linear-gradient(135deg, #17251f, #121c25 75%);
        position: relative;
        overflow: hidden;
    }

    .quality-review-heading {
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 0;
        color: var(--green);
        font: 10px 'DM Mono', monospace;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .quality-review-heading::after {
        content: "EDITORIAL REVIEW";
        margin-left: auto;
        color: rgba(237,242,235,.4);
        font-size: 9px;
        letter-spacing: 1px;
    }

    .st-key-quality-review-content {
        padding: 22px 24px 26px;
        border: 1px solid rgba(200,241,105,.24);
        border-top: 1px solid rgba(200,241,105,.12);
        border-radius: 0 0 15px 15px;
        background: linear-gradient(180deg, rgba(16,23,30,.98), rgba(13,19,25,.98));
        box-shadow: 0 18px 48px rgba(0,0,0,.12);
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] {
        color: #d7e0dc;
        font-size: 13.5px;
        line-height: 1.85;
        overflow-wrap: anywhere;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] h1 {
        margin: 4px 0 20px;
        padding-bottom: 13px;
        border-bottom: 1px solid var(--line);
        color: var(--ink);
        font: 600 clamp(24px, 2.7vw, 32px)/1.25 'Playfair Display', serif;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] h2 {
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 28px 0 12px;
        padding-bottom: 9px;
        border-bottom: 1px solid rgba(41,52,61,.85);
        color: var(--ink);
        font: 600 21px/1.35 'Playfair Display', serif;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] h2::before {
        content: "";
        display: inline-block;
        flex: 0 0 4px;
        width: 4px;
        height: 20px;
        border-radius: 4px;
        background: var(--green);
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] h3 {
        margin: 23px 0 8px;
        color: var(--green);
        font-size: 14px;
        font-weight: 700;
        letter-spacing: .1px;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] p {
        margin: 0 0 15px;
        color: #cbd5d2;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] strong {
        color: #f0f4ee;
        font-weight: 700;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] a {
        color: var(--green);
        text-decoration-color: rgba(200,241,105,.45);
        text-underline-offset: 3px;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] ul,
    .st-key-quality-review-content [data-testid="stMarkdownContainer"] ol {
        margin: 8px 0 20px;
        padding-left: 24px;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] li {
        margin: 7px 0;
        padding-left: 4px;
        color: #cbd5d2;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] li::marker {
        color: var(--green);
        font-weight: 700;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] blockquote {
        margin: 20px 0;
        padding: 14px 18px;
        border-left: 3px solid var(--orange);
        border-radius: 0 10px 10px 0;
        background: rgba(255,112,79,.055);
        color: #dbe5d7;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] blockquote p {
        margin: 0;
        color: #dbe5d7;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 18px 0 24px;
        border: 1px solid var(--line);
        border-radius: 10px;
        overflow: hidden;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] thead tr {
        background: #1a262d;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] th {
        color: var(--green);
        font: 10px 'DM Mono', monospace;
        text-transform: uppercase;
        letter-spacing: .7px;
        border-bottom: 1px solid var(--line);
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] td,
    .st-key-quality-review-content [data-testid="stMarkdownContainer"] th {
        padding: 11px 13px;
        text-align: left;
        border-right: 1px solid rgba(41,52,61,.7);
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] tr:nth-child(even) td {
        background: rgba(255,255,255,.018);
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] hr {
        border: 0;
        border-top: 1px solid var(--line);
        margin: 25px 0;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] :not(pre) > code {
        padding: 2px 6px;
        border: 1px solid #303c45;
        border-radius: 5px;
        background: #182129;
        color: var(--green);
        font: .9em 'DM Mono', monospace;
    }

    .st-key-quality-review-content [data-testid="stMarkdownContainer"] pre {
        padding: 15px;
        border: 1px solid var(--line);
        border-radius: 10px;
        background: #090d11;
        overflow-x: auto;
    }

    /* ===== METRIC CARDS ===== */

    .metric-card {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 16px;
        min-height: 90px;
        box-sizing: border-box;
    }

    .metric-label {
        color: var(--muted);
        font: 10px 'DM Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: var(--ink);
        font-size: 24px;
        font-weight: 700;
        margin-top: 7px;
        overflow-wrap: anywhere;
    }

    /* ===== EXPANDERS & STATUS ===== */

    [data-testid="stExpander"] {
        background: var(--surface) !important;
        border: 1px solid var(--line) !important;
        border-radius: 10px;
    }

    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary p {
        color: var(--ink) !important;
    }

    [data-testid="stStatusWidget"] {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 12px;
    }

    /* ===== FOOTER ===== */

    .footer-note {
        margin-top: 50px;
        border-top: 1px solid var(--line);
        padding-top: 20px;
        font: 10px 'DM Mono', monospace;
        color: var(--muted);
        display: flex;
        justify-content: space-between;
        gap: 12px;
        flex-wrap: wrap;
    }

    /* ===== RESPONSIVE & ACCESSIBILITY ===== */

    @media (max-width: 700px) {
        .topbar {
            align-items: flex-start;
            flex-direction: column;
            margin-bottom: 30px;
        }

        .top-meta {
            text-align: left;
        }

        .hero-title {
            letter-spacing: -1.5px;
        }

        .orbit-label {
            font-size: 8px;
            letter-spacing: 0.5px;
        }

        .report-body {
            padding: 18px;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            animation-duration: 0.01ms !important;
            transition-duration: 0.01ms !important;
        }
    }

    /* ===== QUIET GLASS RESEARCH OVERLAY ===== */
    .research-screen {
        position:fixed; inset:0; z-index:9990; width:100vw; height:100vh; height:100dvh;
        max-width:none; margin:0; padding:clamp(22px,5vw,64px);
        box-sizing:border-box; border:0; border-radius:0;
        display:flex; flex-direction:column; align-items:center; justify-content:center;
        overflow:auto; background:radial-gradient(ellipse at 50% 42%,rgba(200,241,105,.065),transparent 34%),
        radial-gradient(ellipse at 50% 55%,rgba(255,112,79,.045),transparent 44%),rgba(7,11,15,.86);
        -webkit-backdrop-filter:blur(22px); backdrop-filter:blur(22px);
        animation:screen-enter .5s ease-out both;
    }
    .stApp:has(.research-screen) .topbar,
    .stApp:has(.research-screen) .footer-note { opacity:0; pointer-events:none; }
    .research-kicker { color:var(--muted);font:10px 'DM Mono',monospace;letter-spacing:2.5px;text-transform:uppercase;text-align:center;margin-bottom:28px; }
    .research-visual { width:132px;height:132px;margin:0 auto 30px;position:relative;display:flex;align-items:center;justify-content:center; }
    .research-visual .ring { position:absolute;inset:8px;border:2px solid rgba(200,241,105,.38);border-radius:50%;animation:research-ring-spin 150s linear infinite;will-change:transform;box-shadow:0 0 12px rgba(200,241,105,.045); }
    .research-visual .ring-two { inset:-5px;border-width:2px;border-color:rgba(255,112,79,.34);animation-duration:210s;animation-direction:normal; }
    .research-visual .ring-three { inset:25px;border-width:2px;border-style:dashed;border-color:rgba(200,241,105,.24);animation-duration:270s;animation-direction:normal; }
    .research-visual .core { width:48px;height:48px;border-radius:16px;display:flex;align-items:center;justify-content:center;background:rgba(200,241,105,.94);color:#142019;font-size:23px;box-shadow:0 0 34px rgba(200,241,105,.14);z-index:1; }
    .research-title { font-family:'Playfair Display',serif;font-size:clamp(30px,3.8vw,44px);font-weight:600;text-align:center;color:var(--ink);line-height:1.12;margin:0 0 12px;letter-spacing:-1px; }
    .research-subtitle { color:var(--muted);font-family:'DM Sans',sans-serif;font-size:14px;line-height:1.8;text-align:center;max-width:560px;margin:0 auto 30px;overflow-wrap:anywhere; }
    .research-subtitle strong { color:var(--ink);font-weight:500; }
    .stage-progress { width:min(360px,82vw);display:flex;flex-direction:row;gap:6px;margin:0 auto 13px; }
    .stage-segment { height:3px;flex:1;border-radius:10px;background:rgba(255,255,255,.10);transition:background 1.1s cubic-bezier(.22,.61,.36,1),box-shadow 1.1s cubic-bezier(.22,.61,.36,1); }
    .stage-segment.done { background:rgba(200,241,105,.7); }
    .stage-segment.active { background:var(--orange);box-shadow:0 0 8px rgba(255,112,79,.14); }
    .stage-caption { min-height:22px;text-align:center;color:#cbd3d8;font-size:12px;letter-spacing:.15px; }
    .stApp:has(.research-screen) [data-testid="stButton"] { position:fixed;z-index:10000;left:50%;bottom:clamp(20px,5vh,44px);transform:translateX(-50%);width:auto;min-width:132px; }
    .stApp:has(.research-screen) [data-testid="stButton"] button { min-height:42px;padding:0 22px;border-radius:999px;background:rgba(18,24,31,.72)!important;color:#e5e9e5!important;border:1px solid rgba(255,255,255,.15)!important;box-shadow:0 8px 30px rgba(0,0,0,.2);font-size:12px;font-weight:500;backdrop-filter:blur(12px);transition:border-color .2s ease,color .2s ease,background .2s ease; }
    .stApp:has(.research-screen) [data-testid="stButton"] button:hover { border-color:rgba(255,112,79,.55)!important;color:var(--orange)!important;background:rgba(35,24,23,.85)!important; }
    .stApp:has(.research-screen) [data-testid="stAlert"] { display:none; }
    .cancelled-panel { max-width:760px;margin:55px auto;padding:35px;border:1px solid var(--line);border-radius:20px;background:var(--surface);text-align:center;animation:screen-enter .45s ease both; }
    @keyframes screen-enter { from {opacity:0} to {opacity:1} }
    @keyframes segment-breathe { 0%,100% {opacity:.72} 50% {opacity:1} }
    @keyframes research-ring-spin { from {transform:rotate(0deg)} to {transform:rotate(360deg)} }
    @media (max-width:650px) {
        .research-screen { padding:22px 16px 100px; }
        .research-visual { width:112px;height:112px;margin-bottom:25px; }
        .research-subtitle { font-size:12px;margin-bottom:24px; }
    }
    @media (prefers-reduced-motion: reduce) { .research-screen *, .research-screen *::before, .research-screen *::after { animation-duration:.01ms!important;transition-duration:.01ms!important; } }

    </style>
    """,
    unsafe_allow_html=True,
)



# --------------------------------------------------
# HELPERS AND TOP-LEVEL LAYOUT
# --------------------------------------------------

from html import escape
from job_manager import start_research_job, get_research_job, request_stop

STAGES = [
    {"key": "search", "number": "01", "name": "Searching the web", "detail": "Finding credible, relevant sources.", "icon": "search"},
    {"key": "scrape", "number": "02", "name": "Extracting insights", "detail": "Reading source material for deeper context.", "icon": "scrape"},
    {"key": "write", "number": "03", "name": "Writing the report", "detail": "Connecting evidence into a structured report.", "icon": "write"},
    {"key": "critique", "number": "04", "name": "Reviewing quality", "detail": "Checking the report for gaps and clarity.", "icon": "critique"},
]


def as_text(value):
    """Convert LangChain messages and other results into readable text."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if hasattr(value, "content"):
        return as_text(value.content)
    if isinstance(value, dict):
        if "content" in value:
            return as_text(value["content"])
        return str(value)
    return str(value)


def render_topbar():
    st.markdown(
        '''<div class="topbar"><div class="brand"><span class="brand-symbol">✳</span> ORBIT</div><div class="top-meta">MULTI-AGENT RESEARCH SYSTEM &nbsp; / &nbsp; V1.0</div></div>''',
        unsafe_allow_html=True,
    )


def render_hero():
    hero_left, hero_right = st.columns([1.2, 0.8], gap="large")
    with hero_left:
        st.markdown(
            '''<div class="eyebrow">✳ &nbsp; YOUR PERSONAL RESEARCH LAB</div><div class="hero-title">Curiosity,<br>meet <em>intelligence.</em></div><div class="hero-copy">From scattered web discoveries to structured intelligence. Four stages of AI-powered research, working together to turn your questions into reports worth reading.</div>''',
            unsafe_allow_html=True,
        )
    with hero_right:
        st.markdown(
            '''<div class="orbital-card"><div class="orbit-core">✳</div><div class="orbit-label"><span>AGENTS IN ORBIT</span><span>SEARCH / SYNTHESIZE / REVIEW</span></div></div>''',
            unsafe_allow_html=True,
        )


def render_research_form():
    st.markdown(
        '<div class="section-heading"><span class="section-number">01 /</span> Start an investigation</div><div class="section-subtitle">Define a topic. Your agents will take it from there.</div>',
        unsafe_allow_html=True,
    )
    with st.form("research_form", clear_on_submit=False):
        topic = st.text_input(
            "Research topic",
            placeholder="e.g. How are agentic AI systems changing software engineering?",
            label_visibility="collapsed",
        )
        st.caption("NEED INSPIRATION?")
        suggestions = [
            "Agentic AI in software engineering",
            "MCP and the future of AI tool integration",
            "Open-source LLMs for production applications",
        ]
        suggestion_cols = st.columns(3)
        for col, suggestion in zip(suggestion_cols, suggestions):
            with col:
                st.markdown(
                    f'<div style="font-size:11px;color:#929da8;padding:8px 0;line-height:1.5">↗ {escape(suggestion)}</div>',
                    unsafe_allow_html=True,
                )
        submitted = st.form_submit_button("✳  Launch research sequence", type="primary", use_container_width=True)
    if submitted:
        if not topic.strip():
            st.warning("Enter a research topic before launching the sequence.")
        else:
            for key in ("research_result", "research_topic", "research_time", "research_error", "research_cancelled"):
                st.session_state.pop(key, None)
            st.session_state["orbit_job_id"] = start_research_job(topic.strip())
            st.rerun()


def render_agent_cards():
    st.markdown(
        '<div class="section-heading"><span class="section-number">02 /</span> The intelligence pipeline</div><div class="section-subtitle">Four specialized stages. One coherent result.</div>',
        unsafe_allow_html=True,
    )
    agent_data = [
        ("01", "Search Agent", "Discover relevant web information."),
        ("02", "Scrape Agent", "Extract deeper source content."),
        ("03", "Writer Agent", "Synthesize findings into a report."),
        ("04", "Critic Agent", "Evaluate the report for gaps."),
    ]
    cols = st.columns(4, gap="medium")
    for col, (number, name, description) in zip(cols, agent_data):
        with col:
            st.markdown(
                f'<div class="agent-card"><div class="agent-index">{number} / AGENT</div><div class="agent-name">{name}</div><div class="agent-description">{description}</div></div>',
                unsafe_allow_html=True,
            )


def stage_icon(icon_name):
    paths = {
        "search": '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/>',
        "scrape": '<path d="M5 3.5h9l5 5V20a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V4.5a1 1 0 0 1 1-1Z"/><path d="M14 3.5V9h5M7.5 13h7M7.5 16.5h7"/>',
        "write": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4Z"/>',
        "critique": '<path d="M12 3 20 6v5c0 5-3.4 8.2-8 10-4.6-1.8-8-5-8-10V6Z"/><path d="m8.5 12 2.2 2.2 4.8-5"/>',
    }
    return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[icon_name]}</svg>'


def render_processing_screen(job):
    topic = escape(job.get("topic", "your research topic"))
    current = job.get("current_stage")
    completed = set(job.get("completed_stages", []))
    status = job.get("status", "running")
    stage_order = [stage["key"] for stage in STAGES]
    active_stage = next((stage["name"] for stage in STAGES if stage["key"] == current), "Preparing your report")
    segments = []
    # The sequence is intentionally laid out right-to-left: the active segment
    # moves left as each stage completes.
    for stage in STAGES:
        key = stage["key"]
        state = "done" if key in completed else ("active" if key == current else "")
        segments.append(f'<span class="stage-segment {state}"></span>')
    st.markdown(
        f"""<div class="research-screen">
        <div class="research-kicker">ORBIT &nbsp; · &nbsp; RESEARCH IN PROGRESS</div>
        <div class="research-visual"><div class="ring"></div><div class="ring ring-two"></div><div class="ring ring-three"></div><div class="core">✳</div></div>
        <h1 class="research-title">A little thinking in progress.</h1>
        <p class="research-subtitle"><strong>{topic}</strong></p>
        <div class="stage-progress">{''.join(segments)}</div>
        <div class="stage-caption">{escape(active_stage)}</div>
        </div>""",
        unsafe_allow_html=True,
    )
    # Callback runs before Streamlit reruns the page, so the cancellation event
    # is set immediately when the user clicks Stop. Keep the button label static.
    st.button(
        "■  Stop",
        key=f"stop_{job.get('job_id')}",
        disabled=status == "stopping",
        on_click=request_stop,
        args=(job["job_id"],),
    )

def render_report():
    if "research_result" not in st.session_state:
        return
    result = st.session_state["research_result"]
    report = as_text(result.get("report"))
    critique = as_text(result.get("critique"))
    search_results = as_text(result.get("search_results"))
    scraped_content = as_text(result.get("scraped_content"))
    saved_topic = st.session_state.get("research_topic", "Research report")
    st.markdown(
        '<div class="section-heading"><span class="section-number">03 /</span> Research workspace</div><div class="section-subtitle">Your generated intelligence, ready to inspect and export.</div>',
        unsafe_allow_html=True,
    )
    metric_cols = st.columns(3)
    metrics = [("RESEARCH TOPIC", saved_topic), ("PIPELINE STAGES", "04 / 04"), ("GENERATED", st.session_state.get("research_time", "Just now"))]
    for col, (label, value) in zip(metric_cols, metrics):
        with col:
            st.markdown(
                f'<div class="metric-card"><div class="metric-label">{escape(label)}</div><div class="metric-value" style="font-size:15px">{escape(str(value))}</div></div>',
                unsafe_allow_html=True,
            )
    st.markdown(
        f'<div class="report-header"><div class="report-kicker">✳ &nbsp; RESEARCH DOSSIER</div><div class="report-overline">A structured intelligence brief · Generated by ORBIT</div><div class="report-title">{escape(saved_topic)}</div></div>',
        unsafe_allow_html=True,
    )
    if report:
        # A keyed container lets the stylesheet target the rendered Markdown
        # without affecting the rest of the application.
        with st.container(key="report-content"):
            st.markdown(report)
    else:
        st.warning("The writer returned an empty report. Inspect the pipeline output and writer chain.")

    st.markdown('<div class="report-actions-label">Export your research</div>', unsafe_allow_html=True)
    download_cols = st.columns([1, 1, 2])
    with download_cols[0]:
        st.download_button("↓  Download report", data=report or "No report was generated.", file_name="research_report.md", mime="text/markdown", use_container_width=True)
    with download_cols[1]:
        st.download_button("↓  Download critique", data=critique or "No critique was generated.", file_name="research_critique.md", mime="text/markdown", use_container_width=True)

    st.markdown(
        '<div class="quality-review-card"><div class="quality-review-heading">✳ &nbsp; QUALITY REVIEW / CRITIC AGENT</div></div>',
        unsafe_allow_html=True,
    )
    with st.container(key="quality-review-content"):
        st.markdown(critique if critique else "No critique text was returned.")
    with st.expander("01 — View raw search results"):
        st.markdown(search_results or "No search results available.")
    with st.expander("02 — View scraped source content"):
        st.markdown(scraped_content or "No scraped content available.")


def render_footer():
    st.markdown(
        '<div class="footer-note"><span>ORBIT / RESEARCH INTELLIGENCE</span><span>BUILT WITH MULTI-AGENT AI</span><span>THINK DEEPER. RESEARCH BETTER.</span></div>',
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# ROUTE THE PAGE: HOME, ACTIVE RESEARCH, OR RESULTS
# --------------------------------------------------

render_topbar()
job_id = st.session_state.get("orbit_job_id")
job = get_research_job(job_id) if job_id else None

# Handle a very fast job that finished before the first progress-screen render.
if job and job.get("status") == "completed":
    st.session_state["research_result"] = job["result"]
    st.session_state["research_topic"] = job["topic"]
    st.session_state["research_time"] = datetime.now().strftime("%d %b %Y, %H:%M")
    st.session_state.pop("orbit_job_id", None)
    job = None
elif job and job.get("status") == "cancelled":
    st.session_state.pop("orbit_job_id", None)
    st.session_state["research_cancelled"] = True
    job = None
elif job and job.get("status") == "error":
    st.session_state.pop("orbit_job_id", None)
    st.session_state["research_error"] = job.get("error", "Unknown error")
    job = None

if job and job.get("status") in {"running", "stopping"}:
    # The fragment reruns periodically so the progress and Stop button remain live.
    @st.fragment(run_every=1)
    def live_research_panel():
        current_job = get_research_job(job_id)
        if not current_job:
            st.error("The research session could not be found. Please launch it again.")
            return
        status = current_job.get("status")
        if status == "completed":
            st.session_state["research_result"] = current_job["result"]
            st.session_state["research_topic"] = current_job["topic"]
            st.session_state["research_time"] = datetime.now().strftime("%d %b %Y, %H:%M")
            st.session_state.pop("orbit_job_id", None)
            st.rerun()
        if status == "cancelled":
            st.session_state.pop("orbit_job_id", None)
            st.session_state["research_cancelled"] = True
            st.rerun()
        if status == "error":
            st.session_state.pop("orbit_job_id", None)
            st.session_state["research_error"] = current_job.get("error", "Unknown error")
            st.rerun()
        render_processing_screen(current_job)
    live_research_panel()
elif st.session_state.get("research_cancelled"):
    st.markdown(
        '<div class="cancelled-panel"><div class="research-kicker">SEQUENCE HALTED</div><h2 style="color:#edf2eb;font-family:Playfair Display,serif">Research stopped.</h2><p style="color:#929da8">No new research stages will be started. You can launch another investigation whenever you are ready.</p></div>',
        unsafe_allow_html=True,
    )
    if st.button("Start a new investigation", type="primary"):
        st.session_state.pop("research_cancelled", None)
        st.rerun()
elif st.session_state.get("research_error"):
    st.error(f"Research sequence failed: {st.session_state.pop('research_error')}")
    render_hero()
    render_research_form()
    render_agent_cards()
    render_report()
else:
    render_hero()
    render_research_form()
    render_agent_cards()
    render_report()

render_footer()
