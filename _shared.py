"""Shared helpers + Sleek-Liora design system for the Rakuten team Streamlit site."""
import json, os
import streamlit as st

BASE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(BASE, "figures")

# ---- Liora palette -------------------------------------------------------------
CORAL  = "#F0654A"
INDIGO = "#4F46E5"
TEAL   = "#0EA5A4"
AMBER  = "#F59E0B"
PINK   = "#EC4899"
INK    = "#1E293B"
MUTED  = "#64748B"
BG     = "#FBFAF9"
ACCENTS = [CORAL, INDIGO, TEAL, AMBER, PINK]

FAMILY_COLORS = {
    "fusion":      "#7c3aed",
    "transformer": "#4F46E5",
    "multimodal":  "#0EA5A4",
    "classical":   "#64748B",
    "image":       "#F59E0B",
}


@st.cache_data
def raku():
    with open(os.path.join(BASE, "data", "raku.json"), encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def classes():
    with open(os.path.join(BASE, "data", "raku_classes.json"), encoding="utf-8") as f:
        return json.load(f)


def fig(name):
    return os.path.join(FIGDIR, name)


def f3(x):
    return "-" if x is None else f"{x:.3f}"


def _css():
    return f"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"], .stMarkdown, .stApp {{ font-family:'Inter',system-ui,-apple-system,sans-serif; }}
    .stApp {{ background:{BG}; }}
    .block-container {{ max-width:1080px; padding-top:1.5rem; padding-bottom:3rem; }}
    h1 {{ font-weight:800; letter-spacing:-.02em; color:{INK}; }}
    h2, h3 {{ font-weight:700; letter-spacing:-.01em; color:{INK}; }}
    a {{ color:{CORAL}; }}

    /* hero gradient band */
    .rk-hero {{ background:linear-gradient(135deg,#FFF3EF 0%,#F3F1FF 55%,#EAFBFA 100%);
               border:1px solid #F0E8E4; border-radius:22px; padding:26px 30px 22px; margin-bottom:8px;
               box-shadow:0 10px 30px -18px rgba(240,101,74,.45); }}

    /* colored badge / pill */
    .rk-badge {{ display:inline-block; background:#FDE7E1; color:{CORAL}; font-weight:700; font-size:.8rem;
               padding:6px 14px; border-radius:999px; letter-spacing:.02em; }}

    /* metric tiles */
    .rk-tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:14px; margin:6px 0 4px; }}
    .rk-tile {{ position:relative; background:#fff; border:1px solid #EDE9E6; border-radius:18px; padding:16px 18px;
              box-shadow:0 6px 18px -14px rgba(30,41,59,.25); overflow:hidden; transition:transform .15s, box-shadow .15s; }}
    .rk-tile:hover {{ transform:translateY(-3px); box-shadow:0 14px 26px -16px rgba(30,41,59,.35); }}
    .rk-tile::before {{ content:""; position:absolute; left:0; top:0; bottom:0; width:5px; background:var(--c); }}
    .rk-tile .v {{ font-size:1.9rem; font-weight:800; color:var(--c); line-height:1.1; letter-spacing:-.02em; }}
    .rk-tile .l {{ font-size:.8rem; color:{MUTED}; margin-top:4px; font-weight:600; text-transform:uppercase; letter-spacing:.03em; }}

    /* cards */
    .rk-card {{ background:#fff; border:1px solid #EDE9E6; border-radius:18px; padding:18px 22px; height:100%;
              box-shadow:0 8px 22px -16px rgba(30,41,59,.28); transition:transform .15s, box-shadow .15s; }}
    .rk-card:hover {{ transform:translateY(-3px); box-shadow:0 16px 30px -18px rgba(30,41,59,.4); }}
    .rk-card h3 {{ margin-top:0; color:{CORAL}; font-size:1.12rem; }}

    /* callout boxes */
    .rk-note {{ background:#F4F3FF; border-left:4px solid {INDIGO}; border-radius:0 12px 12px 0; padding:13px 18px;
              margin:14px 0; color:#3730A3; font-size:.94rem; }}
    .rk-win  {{ background:#ECFDF9; border-left:4px solid {TEAL}; border-radius:0 12px 12px 0; padding:13px 18px;
              margin:14px 0; color:#0F766E; }}
    .rk-warn {{ background:#FFFBEB; border-left:4px solid {AMBER}; border-radius:0 12px 12px 0; padding:13px 18px;
              margin:14px 0; color:#92400E; }}
    .mono {{ font-family:ui-monospace,Consolas,monospace; background:#F1EFED; padding:1px 6px; border-radius:5px; font-size:.9em; }}

    /* buttons */
    .stButton>button, .stDownloadButton>button, .stLinkButton>a {{
        border-radius:12px; font-weight:600; border:1px solid #EAD9D3; }}
    .stButton>button:hover, .stDownloadButton>button:hover {{ border-color:{CORAL}; color:{CORAL}; }}

    /* divider */
    hr, [data-testid="stDivider"] > div {{ background:linear-gradient(90deg,{CORAL},{INDIGO},{TEAL}) !important;
        height:2px !important; border:none !important; opacity:.5; }}

    /* sidebar */
    section[data-testid="stSidebar"] {{ background:#FFFDFC; border-right:1px solid #EFE9E6; }}
    div[data-testid="stSidebarNav"]::before {{ content:"\\1F6D2  Rakuten Classifier"; display:block;
        padding:14px 18px 6px; font-weight:800; color:{CORAL}; font-size:1.05rem; letter-spacing:-.01em; }}
    div[data-testid="stSidebarNav"] a {{ border-radius:10px; }}

    /* framed figures */
    [data-testid="stImage"] img {{ border-radius:14px; border:1px solid #EDE9E6;
        box-shadow:0 8px 20px -16px rgba(30,41,59,.35); background:#fff; padding:6px; }}
    /* accent on section headers (st.header -> h2) */
    h2 {{ padding-left:14px; border-left:4px solid {CORAL}; }}
    /* pipeline flow */
    .rk-flow {{ display:flex; align-items:stretch; gap:10px; flex-wrap:wrap; margin:12px 0 6px; }}
    .rk-step {{ flex:1 1 180px; background:#fff; border:1px solid #EDE9E6; border-top:4px solid var(--c);
        border-radius:16px; padding:16px 18px; box-shadow:0 8px 22px -16px rgba(30,41,59,.28);
        transition:transform .15s; }}
    .rk-step:hover {{ transform:translateY(-3px); }}
    .rk-step .ic {{ font-size:1.7rem; line-height:1; }}
    .rk-step b {{ display:block; margin:8px 0 2px; color:var(--c); font-size:1.06rem; }}
    .rk-step span {{ color:{MUTED}; font-size:.86rem; }}
    .rk-arrow {{ display:flex; align-items:center; color:{CORAL}; font-size:1.7rem; font-weight:800; }}
    /* multimodal branch flow */
    .rk-mm {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin:12px 0 6px; }}
    .rk-branches {{ display:flex; flex-direction:column; gap:10px; }}
    .rk-mini {{ background:#fff; border:1px solid #EDE9E6; border-left:4px solid var(--c); border-radius:14px;
        padding:11px 16px; box-shadow:0 6px 18px -14px rgba(30,41,59,.25); min-width:210px; transition:transform .15s; }}
    .rk-mini:hover {{ transform:translateY(-2px); }}
    .rk-mini .ic {{ font-size:1.25rem; }}
    .rk-mini b {{ display:block; color:var(--c); font-size:1.02rem; margin-top:2px; }}
    .rk-mini span.t {{ color:{MUTED}; font-size:.82rem; }}
    /* subheaders (st.subheader -> h3): subtle coral accent */
    .stMarkdown h3, [data-testid="stHeading"] h3, h3 {{ padding-left:11px; border-left:3px solid {CORAL}; }}
    /* sidebar nav: hover glow + active accent */
    div[data-testid="stSidebarNav"] a {{ transition:background .15s, box-shadow .15s; }}
    div[data-testid="stSidebarNav"] a:hover {{ background:#FDECE7 !important; box-shadow:0 0 0 1px #F7C9BE inset; }}
    div[data-testid="stSidebarNav"] a[aria-current="page"] {{ background:#FDE7E1 !important;
        box-shadow:inset 3px 0 0 {CORAL}; }}
    </style>"""


def page(title, icon):
    st.set_page_config(page_title=f"{title} · Rakuten Multimodal Classifier",
                       page_icon="🛒", layout="wide", initial_sidebar_state="expanded")
    st.markdown(_css(), unsafe_allow_html=True)


def footer():
    st.divider()
    st.caption(
        "Liora MLE · Project 06 - Rakuten France multimodal product classification (27 classes). "
        "Team: Sandeep Grover · Jonathan Vints · Thomas Maisch.  \n"
        "Dataset 84,916 products (83,502 after removing duplicates). Numbers trace to canonical result files."
    )


def tiles(items):
    """items: list of (value, label). Renders colorful gradient-accent metric tiles."""
    cells = "".join(
        f'<div class="rk-tile" style="--c:{ACCENTS[i % len(ACCENTS)]}">'
        f'<div class="v">{val}</div><div class="l">{lab}</div></div>'
        for i, (val, lab) in enumerate(items)
    )
    st.markdown(f'<div class="rk-tiles">{cells}</div>', unsafe_allow_html=True)
