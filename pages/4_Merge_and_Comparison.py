"""Merge (fusion) & model comparison - Thomas Maisch (EfficientNet-B0 + XLM-RoBERTa)."""
import streamlit as st
import pandas as pd
from _shared import page, footer, tiles, fig

page("Merge & Comparison", "🔗")

st.title("🔗 Merge (fusion) & model comparison")
st.caption("Owner: **Thomas Maisch** · late fusion of the image and text branches -> the team's best model.")

tiles([
    ("0.9034", "Multimodal (weighted-F1)"),
    ("0.8144", "Multimodal benchmark"),
    ("0.4%",   "Params trained (fusion head)"),
    ("27",     "Classes"),
])

st.subheader("1 · Multimodal architecture")
st.markdown(
    "**Late fusion**: a frozen **EfficientNet-B0** (image -> 1280-d) and a frozen **XLM-RoBERTa** "
    "(text -> 768-d) are concatenated to **2048-d**, then a small **fusion head** (Linear · ReLU · Dropout) "
    "is trained over the 27 classes. Only **1,062,939 of 283,804,621 parameters (0.4%)** are trainable.")
st.image(fig("thomas/slide_07.png"), use_container_width=True)

st.subheader("2 · Final leaderboard (weighted-F1)")
lb = pd.DataFrame({
    "Model": ["CNN from scratch", "ResNet50 benchmark", "Our image model", "Text benchmark",
              "Multimodal benchmark", "Our text model", "Our multimodal model"],
    "Weighted-F1": [0.3093, 0.5534, 0.6515, 0.8113, 0.8144, 0.87, 0.9034],
    "Stage": ["image", "image", "image", "text", "fusion", "text", "fusion"],
})
st.dataframe(lb, use_container_width=True, hide_index=True)
st.caption("Our multimodal model (0.9034) beats the DataScientest multimodal benchmark (0.8144) and the text-only model.")

st.subheader("3 · Does fusion actually help? (5-seed ablation)")
st.markdown(
    "Image-only **0.6577** · Text-only **0.8927** · Full multimodal **0.9029** (mean ± SD over 5 seeds). "
    "Text carries most of the signal; the image branch adds a **small but robust** lift, concentrated on the "
    "classes where the picture disambiguates (books, magazines, posters, collectibles).")
c1, c2 = st.columns(2)
with c1: st.image(fig("thomas/slide_10.png"), use_container_width=True, caption="Fusion gain ablation (5 seeds).")
with c2: st.image(fig("thomas/slide_11.png"), use_container_width=True, caption="Per-class contribution of the image modality.")

st.subheader("4 · Multimodal confusion matrix")
st.image(fig("thomas/slide_09.png"), use_container_width=True, caption="27×27 confusion (% per true class) - clean diagonal.")

st.markdown(
    '<div class="rk-win"><b>Result.</b> The fused EfficientNet-B0 + XLM-RoBERTa model reaches '
    '<b>weighted-F1 0.9034</b> - the team\'s strongest classifier.</div>', unsafe_allow_html=True)
footer()
