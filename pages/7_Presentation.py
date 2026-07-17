"""Presentation - the full team slide deck (business case, data, text, image, multimodal fusion)."""
import os
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Presentation", "🖥️")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "slides", "presentation.html")
PDF = os.path.join(BASE, "downloads", "Rakuten_Presentation.pdf")
FULL = "http://82.29.180.70:8090/rakuten-deliverables/rakuten_presentation.html"

st.title("Presentation")
st.caption("The full team slide deck: business case, data exploration, text and image modelling, and "
           "multimodal fusion.")

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.link_button("🔳 Open fullscreen (new tab)", FULL, use_container_width=True)
with c2:
    if os.path.exists(PDF):
        with open(PDF, "rb") as f:
            st.download_button("⬇ Download slides (PDF)", f.read(),
                               file_name="Rakuten_Presentation.pdf", mime="application/pdf",
                               use_container_width=True)
with c3:
    with open(HTML, "rb") as f:
        st.download_button("⬇ Download slides (HTML)", f.read(),
                           file_name="Rakuten_Presentation.html", mime="text/html",
                           use_container_width=True)

st.markdown('<div class="rk-note">Use <b>Open fullscreen</b> for the best view. In the embed below, click inside the deck '
            'and use the <b>Previous / Next</b> buttons at the bottom bar, the <b>&larr; / &rarr;</b> arrow keys, or press <b>F</b>.</div>',
            unsafe_allow_html=True)

with open(HTML, encoding="utf-8") as f:
    deck = f.read()
components.html(deck, height=820, scrolling=True)
footer()
