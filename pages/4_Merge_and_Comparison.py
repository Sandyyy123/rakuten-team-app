"""Placeholder — Merge (fusion) & model comparison (Jonathan Vints)."""
import streamlit as st
from _shared import page, footer

page("Merge & Comparison", "🔗")
st.title("Merge (fusion) & model comparison")
st.info("🚧 **Placeholder — this section is owned by Jonathan Vints.**\n\n"
        "It covers the **multimodal fusion** of the text and image branches (**Text + Image**), and a "
        "**comparison of all models** on one leaderboard (weighted-F1, macro-F1, accuracy) plus the final "
        "confusion matrix.")
st.markdown("**Depends on:** the *Text modelling* and *Image processing & modelling* pages.")
footer()
