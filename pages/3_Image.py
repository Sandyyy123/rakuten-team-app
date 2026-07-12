"""Placeholder — Image branch (Thomas Maisch)."""
import streamlit as st
from _shared import page, footer

page("Image", "🖼️")
st.title("Image branch")
st.info("🚧 **Placeholder — this section is owned by Thomas Maisch.**\n\n"
        "It covers the **image branch only**: a CNN (e.g. ResNet18 / EfficientNet) that turns each product "
        "photo into image features and reports the image-only performance. These image features are then "
        "passed to Jonathan for the multimodal fusion.")
st.markdown("**Feeds into:** the *Modelling & Fusion* page, where the image features are fused with the "
            "text model.")
footer()
