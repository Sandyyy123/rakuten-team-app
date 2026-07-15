"""Image processing & modelling - Thomas Maisch (crop -> EfficientNet-B0)."""
import streamlit as st
from _shared import page, footer, tiles, fig

page("Image Modelling", "🖼️")
GH = "https://github.com/DataScientest-Studio/apr26_bds_int_rakuten/tree/Thomas"

st.title("🖼️ Image processing & modelling")
st.caption("Owner: **Thomas Maisch** · from a from-scratch CNN to a tuned EfficientNet-B0.")

tiles([
    ("0.6515", "Image model (weighted-F1)"),
    ("0.5534", "ResNet50 benchmark"),
    ("0.31",   "CNN from scratch"),
    ("EfficientNet-B0", "Backbone"),
])

st.subheader("1 · Image preprocessing")
st.markdown(
    "Most Rakuten photos sit inside a wide white border. A **corner-sampling crop** (average the four "
    "corner pixels -> treat as background -> bounding box) isolates the product, then images are resized "
    "to a fixed CNN input and each path is attached to the text-preprocessed dataframe.")
st.image(fig("thomas/slide_01.png"), use_container_width=True, caption="Raw product image vs the model input after cropping / resizing.")

st.subheader("2 · Do we even need a pretrained model?")
st.markdown(
    "A **SimpleCNN trained from scratch** plateaus around **0.31 weighted-F1**, and augmentation / class-weights / "
    "weighted-sampler do **not** help. Conclusion: transfer learning is required.")
st.image(fig("thomas/slide_02.png"), use_container_width=True)

st.subheader("3 · Why EfficientNet-B0 instead of ResNet50")
st.markdown(
    "EfficientNet-B0 is **~5× smaller** than the benchmark's ResNet50 (5.3M vs 25.6M params) and **more "
    "accurate** on ImageNet (77.1% vs 74.9%) - so it is the backbone of choice "
    "(`timm.create_model('efficientnet_b0', pretrained=True, num_classes=27)`).")
st.image(fig("thomas/slide_13.png"), use_container_width=True)

st.subheader("4 · Tuning - ablation study")
st.markdown(
    "A ~25-combination grid over **freezing / augmentation / class-weights / sampler / classifier** lifts the "
    "image model from the 0.31 baseline to **0.5482** at 10k, and the final model reaches **weighted-F1 0.6515** "
    " -  above the ResNet50 benchmark (0.5534).")
c1, c2 = st.columns(2)
with c1: st.image(fig("thomas/slide_03.png"), use_container_width=True, caption="Ablation over ~25 combinations.")
with c2: st.image(fig("thomas/slide_04.png"), use_container_width=True, caption="Final image model - val F1 ≈ 0.65.")

st.subheader("5 · Where the image model fails, and what it looks at")
st.markdown(
    "Errors concentrate in two **visually similar** families - figurines/toys/games/models and "
    "books/magazines. **GradCAM** shows the CNN attends to sensible regions: the title-text band on book "
    "covers, the object itself on 3D items.")
c3, c4 = st.columns(2)
with c3: st.image(fig("thomas/slide_05.png"), use_container_width=True, caption="Confusion within the two error clusters.")
with c4: st.image(fig("thomas/slide_06.png"), use_container_width=True, caption="GradCAM explanations.")

st.markdown(f'<div class="rk-note">Code &amp; trained EfficientNet-B0 on Thomas\'s branch -> <a href="{GH}">{GH}</a></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="rk-win"><b>Hand-off to fusion.</b> The frozen EfficientNet-B0 image features (1280-d) are '
    'combined with the XLM-RoBERTa text features on the <b>Merge &amp; comparison</b> page.</div>',
    unsafe_allow_html=True)
footer()
