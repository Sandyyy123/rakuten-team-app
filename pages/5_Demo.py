"""Demo — the full model runs as a Streamlit app you can open on HuggingFace OR run locally."""
import os, json
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Demo", "🔮")

# The full fused CamemBERT + image model runs as a standalone Streamlit app. It is too big for
# Streamlit Cloud (~1 GB), so it lives on a HuggingFace Space (free 16 GB) and/or runs locally.
HF_USER     = "<your-username>"     # your HuggingFace username (or org, e.g. "liora")
HF_DEMO_URL = ""                    # after deploy: f"https://{HF_USER}-rakuten-liora-app.hf.space"
SPACE_REPO  = f"https://huggingface.co/spaces/{HF_USER}/rakuten-liora-app"

st.title("🔮 Live demo — predict a product's category")
st.caption("Type a French product title (and/or upload an image) → the fine-tuned CamemBERT + image "
           "model predicts one of 27 categories, with top-3 confidence.")

st.markdown("#### Two ways to run the live demo")
c1, c2 = st.columns(2)
with c1:
    st.markdown(
        '<div class="rk-tile" style="--c:#F0654A"><b>☁️ On HuggingFace</b><br>'
        'Free 16 GB Space — public URL, nothing to install. Best for sharing.</div>',
        unsafe_allow_html=True)
with c2:
    st.markdown(
        '<div class="rk-tile" style="--c:#4F46E5"><b>💻 Locally</b><br>'
        'Same app on your own machine — private, uses your RAM/GPU, no account.</div>',
        unsafe_allow_html=True)

# ---- HuggingFace (embedded live) --------------------------------------------
st.markdown("### ☁️ Open it on HuggingFace")
if HF_DEMO_URL:
    st.markdown(
        f'<div class="rk-win"><b>Live now.</b> Running the full fused model on our HuggingFace Space '
        f'(16 GB). <a href="{HF_DEMO_URL}" target="_blank"><b>Open full-screen →</b></a></div>',
        unsafe_allow_html=True)
    components.iframe(HF_DEMO_URL, height=900, scrolling=True)
else:
    st.info("The HuggingFace Space (`rakuten-liora-app`) is being set up — this page will embed it "
            "here and link to it full-screen as soon as it's live.")

# ---- Locally -----------------------------------------------------------------
st.markdown("### 💻 Run it locally")
st.markdown("Clone the Space (or the `hf_space/` folder) and start Streamlit — the full model runs on "
            "your machine, privately:")
st.code(f"git clone {SPACE_REPO}\ncd rakuten-liora-app\npip install -r requirements.txt\n"
        "streamlit run app.py        # -> http://localhost:8501", language="bash")

# ---- what it classifies ------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMP = os.path.join(ROOT, "demo_samples")
sp = os.path.join(SAMP, "samples.json")
if os.path.exists(sp):
    st.markdown("#### What the demo classifies — 8 real Rakuten products")
    samples = json.load(open(sp, encoding="utf-8"))
    cols = st.columns(4)
    for i, s in enumerate(samples):
        with cols[i % 4]:
            ip = os.path.join(SAMP, s["image"])
            if os.path.exists(ip):
                st.image(ip, use_container_width=True, caption=f"{s['name']} · {s['code']}")
st.caption("Under the hood: text branch (fine-tuned CamemBERT) + image branch (CNN), combined by "
           "late fusion → top-3 categories with confidence.")
footer()
