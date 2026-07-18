"""Merge (fusion) & model comparison - Thomas Maisch (EfficientNet-B0 + XLM-RoBERTa)."""
import streamlit as st
import pandas as pd
from _shared import page, footer, tiles, fig

page("Merge & Comparison", "🔗")

st.title("🔗 Merge (fusion) & model comparison")
st.caption("Owner: **Thomas Maisch** · late fusion of the image and text branches -> the team's best model.")

tiles([
    ("0.8984", "Multimodal (weighted-F1)"),
    ("#16",    "Public leaderboard (0.8902)"),
    ("0.8144", "Multimodal benchmark"),
    ("27",     "Classes"),
])

st.subheader("1 · Multimodal architecture")
st.markdown(
    "**Late fusion**: a frozen **EfficientNet-B0** (image -> 1280-d) and a frozen **XLM-RoBERTa** "
    "(text -> 768-d) are concatenated to **2048-d**, then a small **fusion head** (Linear · ReLU · Dropout) "
    "is trained over the 27 classes. Only **1,062,939 of 283,804,621 parameters (0.4%)** are trainable.")
st.image(fig("thomas/tm_architecture_light.png"), use_container_width=True)

st.subheader("2 · Final leaderboard (weighted-F1)")
lb = pd.DataFrame({
    "Model": ["CNN from scratch", "ResNet50 benchmark", "Our image model", "Text benchmark",
              "Multimodal benchmark", "Our text model", "Our multimodal model"],
    "Weighted-F1": [0.3093, 0.5534, 0.6515, 0.8113, 0.8144, 0.87, 0.8984],
    "Stage": ["image", "image", "image", "text", "fusion", "text", "fusion"],
})
st.dataframe(lb, use_container_width=True, hide_index=True)
st.caption("Our multimodal model (0.8984, mean over 5 seeds) beats the DataScientest multimodal benchmark (0.8144) and the text-only model.")

st.subheader("3 · Public benchmark ranking")
st.markdown(
    "Submitted to the public **Rakuten France Multimodal Product Data Classification** leaderboard as "
    "**Sandeep_Jonathan_Thomas_Liora** (16 Jul 2026): **public score 0.8902, rank #16**.")
rk = pd.DataFrame({
    "Rank": [1, 5, 9, 15, 16],
    "Team": ["Gaby & xiaosong & Caeles", "ionch", "forgeros", "julienC",
             "Sandeep_Jonathan_Thomas_Liora"],
    "Public score": [0.9273, 0.9074, 0.9011, 0.8903, 0.8902],
})
st.dataframe(rk, use_container_width=True, hide_index=True)
st.caption("Top of the public leaderboard, with our team highlighted at #16.")

st.subheader("4 · Does fusion actually help? (5-seed ablation)")
st.markdown(
    "Image-only **0.6787** · Text-only **0.8761** · Full multimodal **0.8985** (mean over 5 seeds). "
    "Text carries most of the signal; the image branch adds a **small but robust** lift, concentrated on the "
    "classes where the picture disambiguates (books, magazines, posters, collectibles).")
c1, c2 = st.columns(2)
with c1: st.image(fig("thomas/tm_fusion_gain.png"), use_container_width=True, caption="Fusion gain ablation (5 seeds).")
with c2: st.image(fig("thomas/tm_perclass_gain.png"), use_container_width=True, caption="Per-class contribution of the image modality.")

st.subheader("5 · Multimodal confusion matrix")
st.image(fig("thomas/tm_mm_confusion.png"), use_container_width=True, caption="27×27 confusion (% per true class) - clean diagonal.")

st.markdown(
    '<div class="rk-win"><b>Result.</b> The fused EfficientNet-B0 + XLM-RoBERTa model reaches '
    '<b>weighted-F1 0.8984</b> (5-seed mean) - the team\'s strongest classifier, ranked '
    '<b>#16</b> on the public leaderboard.</div>', unsafe_allow_html=True)
footer()
