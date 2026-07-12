"""Placeholder — Modelling & multimodal fusion (Jonathan Vints)."""
import streamlit as st
from _shared import page, footer

page("Modelling & Fusion", "🤖")
st.title("Modelling & multimodal fusion")
st.info("🚧 **Placeholder — this section is owned by Jonathan Vints.**\n\n"
        "It covers the **classical models** (Logistic Regression, LinearSVC, XGBoost on TF-IDF features), "
        "the **deep-learning text models** (fine-tuned CamemBERT), and the **multimodal fusion** of the text "
        "model with Thomas's image branch — reporting weighted-F1 and macro-F1, the leaderboard, confusion "
        "matrix and the final multimodal results.")
st.markdown("**Inputs to this stage:** the TF-IDF feature matrix from the *Data & EDA* page "
            "(~67,900 train / ~17,000 test rows · 20,000 sparse features + `desc_missing` + length features), "
            "and the image features from the *Image* page.")
footer()
