"""Placeholder — Image processing & modelling (Thomas Maisch)."""
import streamlit as st
from _shared import page, footer

page("Image Modelling", "🖼️")
st.title("Image processing & modelling")
st.info("🚧 **Placeholder — this section is owned by Thomas Maisch.**\n\n"
        "It covers **image preprocessing** (resize, crop, augmentation) and the **image model** "
        "(a CNN — ResNet / EfficientNet) that turns each product photo into image features and reports the "
        "image-only performance.")
st.markdown('<div class="rk-note">Feeds into the <b>Merge &amp; comparison</b> page, where the image features '
            'are fused with the text model.</div>', unsafe_allow_html=True)
footer()
