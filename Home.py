"""Home — project landing. Data & EDA is fully built (Sandeep Grover); other sections are placeholders."""
import streamlit as st
from _shared import page, footer, tiles, raku

page("Home", "🛒")
R = raku(); s = R["stats"]
import os as _os, base64 as _b64
_logo=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),"report_figs","liora_logo.png")
if _os.path.exists(_logo):
    _b=_b64.b64encode(open(_logo,"rb").read()).decode()
    st.markdown(f'<img src="data:image/png;base64,{_b}" alt="Liora" '
                'style="width:240px;height:auto;display:block;margin:2.4rem 0 0.6rem">',
                unsafe_allow_html=True)

st.markdown('<span class="rk-badge">Liora MLE · Project 06 · Team project</span>', unsafe_allow_html=True)
st.title("Rakuten France — Multimodal Product Classification")
st.markdown("#### Sorting 84,916 products into 27 categories from their French titles and photos")
st.markdown(
    "A team project on the public **Rakuten France** multimodal classification challenge. The goal: predict "
    "each product's category (`prdtypecode`) from its **text** (title + description) and its **image**. This "
    "app is the interactive restitution — one page per project stage.")

tiles([
    (f"{s['n_products']:,}",             "Products"),
    (str(s["n_classes"]),                "Categories"),
    (f"{s['imbalance_ratio']}×",         "Class imbalance"),
    (f"{s['pct_missing_description']}%", "Missing description"),
    ("~81%",                             "French text"),
])
st.divider()

st.subheader("Project sections")
st.markdown(
    "- ✅ **Data & EDA** — business case, data exploration and text pre-processing *(Sandeep Grover — complete)*\n"
    "- 🚧 **Modelling & Fusion** — classical & deep-learning models + multimodal fusion *(Jonathan Vints — placeholder)*\n"
    "- 🚧 **Image** — image branch / CNN *(Thomas Maisch — placeholder)*\n"
    "- 🚧 **Demo** — live prediction on new input *(team — once models are trained)*\n"
    "- 📄 **Report** — the written project report (PDF / Word)")

st.markdown('<div class="rk-note"><b>Start here:</b> open <b>Data & EDA</b> in the sidebar — it is the fully '
            'built section (business case, five statistical findings with figures, and the TF-IDF '
            'pre-processing pipeline). The other stages are placeholders for the teammates to complete.</div>',
            unsafe_allow_html=True)
footer()
