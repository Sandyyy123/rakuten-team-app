"""Shared helpers for the Rakuten team Streamlit site (mirrors the HTML/JS site)."""
import json, os
import streamlit as st

BASE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(BASE, "figures")

RED   = "#bf0000"
INK   = "#0f172a"
MUTED = "#64748b"
OK    = "#059669"
CRIM  = "#bf0000"

FAMILY_COLORS = {
    "fusion":      "#7c3aed",
    "transformer": "#2563eb",
    "multimodal":  "#0891b2",
    "classical":   "#64748b",
    "image":       "#d97706",
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


def page(title, icon):
    st.set_page_config(page_title=f"{title} · Rakuten Multimodal Classifier",
                       page_icon="🛒", layout="wide",
                       initial_sidebar_state="expanded")
    st.markdown(f"""<style>
      .block-container {{max-width:1080px; padding-top:1.2rem}}
      h1,h2,h3 {{color:{INK}}}
      .rk-badge {{display:inline-block;background:#fee2e2;color:{RED};font-weight:700;
                 font-size:.8rem;padding:4px 12px;border-radius:20px;letter-spacing:.02em}}
      .rk-note {{background:#f1f5f9;border-left:4px solid {RED};border-radius:0 8px 8px 0;
                padding:12px 16px;margin:14px 0;color:#334155;font-size:.94rem}}
      .rk-win  {{background:#ecfdf5;border-left:4px solid {OK};border-radius:0 8px 8px 0;
                padding:12px 16px;margin:14px 0;color:#065f46}}
      .rk-warn {{background:#fffbeb;border-left:4px solid #d97706;border-radius:0 8px 8px 0;
                padding:12px 16px;margin:14px 0;color:#92400e}}
      .rk-card {{background:#fff;border:1px solid #e2e8f0;border-radius:12px;
                padding:16px 20px;height:100%;box-shadow:0 1px 3px rgba(0,0,0,.04)}}
      .rk-card h3 {{margin-top:0;color:{RED}}}
      .mono {{font-family:ui-monospace,Consolas,monospace;background:#f1f5f9;
             padding:1px 5px;border-radius:4px;font-size:.9em}}
      div[data-testid="stSidebarNav"]::before {{
        content:"🛒 Rakuten Classifier"; display:block; padding:12px 18px 4px;
        font-weight:800; color:{RED}; font-size:1.05rem}}
    </style>""", unsafe_allow_html=True)


def footer():
    st.divider()
    st.caption(
        "Liora MLE · Project 06 — Rakuten France multimodal product classification (27 classes). "
        "Team: Sandeep Grover · Jonathan Vints · Thomas Maisch.  \n"
        "All metrics computed on the full 84,916-product corpus (test split). "
        "Numbers trace to canonical result files (`raku.json`)."
    )


def tiles(items):
    """items: list of (value, label). Renders native metric cards in columns."""
    cols = st.columns(len(items))
    for c, (val, lab) in zip(cols, items):
        c.metric(lab, val)
