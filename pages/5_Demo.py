"""Demo — the live full model is hosted on a HuggingFace Space (16 GB). This page embeds/links it."""
import os, json
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer, CORAL

page("Demo", "🔮")

# The full fused CamemBERT + image model runs on a HuggingFace Space (16 GB RAM) — Streamlit Cloud
# (~1 GB) is too small for CamemBERT. After you create the Space, paste its URL here:
HF_DEMO_URL = ""  # e.g. "https://<your-username>-rakuten-multimodal.hf.space"

st.title("🔮 Live demo — predict a product's category")
st.caption("Type a French product title (and/or upload an image) → the fine-tuned CamemBERT + image "
           "model predicts one of 27 categories. Runs live below.")

if HF_DEMO_URL:
    st.markdown(
        f'<div class="rk-win"><b>Live model.</b> The demo below runs the full fused model on our '
        f'HuggingFace Space (16 GB). '
        f'<a href="{HF_DEMO_URL}" target="_blank"><b>Open it full-screen in a new tab →</b></a></div>',
        unsafe_allow_html=True)
    components.iframe(HF_DEMO_URL, height=920, scrolling=True)
else:
    st.markdown(
        '<div class="rk-warn"><b>Live demo is being deployed.</b> The full fused CamemBERT + image model '
        'needs ~2–4 GB RAM, so it runs on a <b>HuggingFace Space (free, 16 GB)</b> — Streamlit Cloud '
        '(~1 GB) is too small for CamemBERT. This page will embed the live demo here (and link to it '
        'full-screen) as soon as the Space is up and the trained model files arrive.</div>',
        unsafe_allow_html=True)

    # preview: the real Rakuten products the demo will classify
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SAMP = os.path.join(ROOT, "demo_samples")
    sp = os.path.join(SAMP, "samples.json")
    if os.path.exists(sp):
        st.markdown("#### What the demo will classify — 8 real Rakuten products")
        samples = json.load(open(sp, encoding="utf-8"))
        cols = st.columns(4)
        for i, s in enumerate(samples):
            with cols[i % 4]:
                ip = os.path.join(SAMP, s["image"])
                if os.path.exists(ip):
                    st.image(ip, use_container_width=True, caption=f"{s['name']} · {s['code']}")

    st.markdown("**How the live demo works:** text branch (fine-tuned CamemBERT) + image branch (CNN), "
                "combined by late fusion, returns the top-3 categories with confidence.")

footer()
