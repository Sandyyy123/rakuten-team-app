"""Run the model - opens the live classifier: your local instance, or the public Hostinger one."""
import os, json
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Run the model", "🔮")

# Where the full classifier is served. Local = your machine (./run_local.sh). VPS = public Hostinger.
LOCAL_URL = "http://localhost:8530"   # your local instance
VPS_URL   = ""                        # public Hostinger URL, set once deployed (e.g. http://82.29.180.70:8501)

st.title("🔮 Run the model - predict a product's category")
st.caption("Type a French product title (and/or upload an image) → the fine-tuned XLM-RoBERTa + image "
           "model predicts one of 27 categories, with top-3 confidence. Open it below.")

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="rk-tile" style="--c:#F0654A"><b>💻 On your machine</b><br>'
                'Free, private, uses your GPU/RAM. Start it, then open the local address.</div>',
                unsafe_allow_html=True)
    st.link_button("▶ Open local instance", LOCAL_URL, use_container_width=True)
    st.caption(f"Address: {LOCAL_URL} - works while `./run_local.sh` is running on your machine.")
with c2:
    st.markdown('<div class="rk-tile" style="--c:#4F46E5"><b>☁️ On Hostinger (public)</b><br>'
                'A shareable link anyone can open - the grader, teammates, any device.</div>',
                unsafe_allow_html=True)
    if VPS_URL:
        st.link_button("▶ Open public demo", VPS_URL, use_container_width=True)
        st.caption(f"Public address: {VPS_URL}")
    else:
        st.button("▶ Open public demo", use_container_width=True, disabled=True,
                  help="Set VPS_URL once the demo is deployed to the Hostinger VPS.")
        st.caption("Public link coming once it's deployed to the VPS.")

# embed the public one inline if it's available over https
if VPS_URL.startswith("https://"):
    st.markdown("### Live (embedded)")
    components.iframe(VPS_URL, height=900, scrolling=True)

st.divider()
st.markdown("#### Start the local instance")
st.code("cd /root/AI/liora_projects/06_rakuten_multimodal/hf_space\n"
        "./run_local.sh          # -> http://localhost:8530", language="bash")

# what it classifies
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMP = os.path.join(ROOT, "demo_samples")
sp = os.path.join(SAMP, "samples.json")
if os.path.exists(sp):
    st.markdown("#### What the model classifies - 8 real Rakuten products")
    samples = json.load(open(sp, encoding="utf-8"))
    cols = st.columns(4)
    for i, s in enumerate(samples):
        with cols[i % 4]:
            ip = os.path.join(SAMP, s["image"])
            if os.path.exists(ip):
                st.image(ip, use_container_width=True, caption=f"{s['name']} · {s['code']}")
st.caption("Under the hood: text branch (XLM-RoBERTa) + image branch (EfficientNet-B0), late fusion "
           "→ top-3 categories with confidence.")
footer()
