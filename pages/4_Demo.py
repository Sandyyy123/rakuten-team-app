"""Placeholder — live prediction demo (team, once models are trained)."""
import streamlit as st
from _shared import page, footer

page("Demo", "🔮")
st.title("Live prediction demo")
st.info("🚧 **Placeholder — to be wired to the trained model.**\n\n"
        "The final app will let the jury enter a product title (and optionally an image) and return the "
        "predicted product-type category from the trained CamemBERT + image fusion model.")
st.markdown("This page depends on the trained models from the *Modelling* and *Image & Fusion* sections.")
footer()
