"""Placeholder — Modelling section (Jonathan Vints)."""
import streamlit as st
from _shared import page, footer

page("Modelling", "🤖")
st.title("Modelling — classical & deep learning")
st.info("🚧 **Placeholder — this section is owned by Jonathan Vints.**\n\n"
        "It will compare classical models (Logistic Regression, LinearSVC, XGBoost on TF-IDF features) "
        "against deep-learning text models (fine-tuned CamemBERT), reporting weighted-F1 and macro-F1 on "
        "the held-out test set.")
st.markdown("**Input to this stage:** the TF-IDF feature matrix handed over from the *Data & EDA* page "
            "(~67,900 train / ~17,000 test rows · 20,000 sparse features + `desc_missing` + length features).")
footer()
