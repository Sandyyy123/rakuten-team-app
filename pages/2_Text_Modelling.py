"""Placeholder — Text modelling (Jonathan Vints)."""
import streamlit as st
from _shared import page, footer

page("Text Modelling", "🤖")
st.title("Text modelling")
st.info("🚧 **Placeholder — this section is owned by Jonathan Vints.**\n\n"
        "It covers the **classical models** (Logistic Regression, LinearSVC, XGBoost on the TF-IDF features) "
        "and the **deep-learning text models** (fine-tuned CamemBERT), reported on **weighted-F1** and macro-F1.")
st.markdown("**Input to this stage:** the TF-IDF feature matrix from the *Data & EDA* page "
            "(~66,800 train / ~16,700 test · 20,000 features + `desc_missing` + length features).")
st.markdown('<div class="rk-note">Feeds into the <b>Merge &amp; comparison</b> page, where the best text '
            'model is fused with the image branch.</div>', unsafe_allow_html=True)
footer()
