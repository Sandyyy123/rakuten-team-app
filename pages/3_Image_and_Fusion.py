"""Placeholder — Image branch, fusion & results (Thomas Maisch)."""
import streamlit as st
from _shared import page, footer

page("Image & Fusion", "🖼️")
st.title("Image branch, multimodal fusion & results")
st.info("🚧 **Placeholder — this section is owned by Thomas Maisch.**\n\n"
        "It will add the image branch (ResNet18 CNN), fuse it with the text model (weighted late fusion / "
        "RoBERTa), and present the final multimodal results: leaderboard, confusion matrix, per-class F1 and "
        "the conclusion.")
st.markdown("**Depends on:** the text models from the *Modelling* page and the feature matrix from *Data & EDA*.")
footer()
