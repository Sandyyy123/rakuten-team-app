"""Demo — live multimodal prediction (CamemBERT text + CNN image, late fusion)."""
import os, json
import numpy as np
import streamlit as st
from _shared import page, footer

page("Demo", "🔮")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS, SAMP = os.path.join(ROOT, "models"), os.path.join(ROOT, "demo_samples")

# CONFIG (teammates set these)
CAMEMBERT_DIR = os.path.join(MODELS, "camembert")
TEXT_MAXLEN, IMAGE_WEIGHT, IMAGE_ARCH, IMAGE_SIZE = 256, 0.30, "resnet18", 224
IMG_MEAN, IMG_STD = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
IMAGE_WEIGHTS = os.path.join(MODELS, "image_model.pth")
CLASS_ORDER = json.load(open(os.path.join(MODELS, "class_order.json")))
LABELS_EN = json.load(open(os.path.join(MODELS, "labels_en.json")))
TEXT_READY = os.path.isdir(CAMEMBERT_DIR)
IMG_READY = os.path.exists(IMAGE_WEIGHTS)

st.title("🔮 Live demo — predict a product's category")
st.caption("Type a French product title (and/or upload an image) → the model predicts the category. "
           "Fine-tuned CamemBERT (text) + CNN (image), late fusion.")

if not TEXT_READY:
    st.markdown('<div class="rk-warn"><b>Model not loaded here.</b> The trained CamemBERT + image files '
                'go in <code>models/</code> (see <code>models/CHECKLIST.md</code>). The full model needs '
                '~2–4 GB RAM, so run this app on a <b>HuggingFace Space (free, 16 GB)</b> — Streamlit '
                'Cloud (~1 GB) is too small for CamemBERT. The examples below are ready to click.</div>',
                unsafe_allow_html=True)

@st.cache_resource(show_spinner="Loading CamemBERT…")
def load_text():
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    return AutoTokenizer.from_pretrained(CAMEMBERT_DIR), AutoModelForSequenceClassification.from_pretrained(CAMEMBERT_DIR).eval()

@st.cache_resource(show_spinner="Loading image model…")
def load_image():
    import torch, torchvision
    from torchvision import transforms
    n = len(CLASS_ORDER)
    if IMAGE_ARCH == "resnet18":
        m = torchvision.models.resnet18(weights=None); m.fc = torch.nn.Linear(m.fc.in_features, n)
    else:
        m = torchvision.models.efficientnet_b0(weights=None); m.classifier[1] = torch.nn.Linear(m.classifier[1].in_features, n)
    m.load_state_dict(torch.load(IMAGE_WEIGHTS, map_location="cpu")); m.eval()
    tf = transforms.Compose([transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)), transforms.ToTensor(), transforms.Normalize(IMG_MEAN, IMG_STD)])
    return m, tf

def text_probs(t):
    import torch
    tok, model = load_text(); enc = tok(t, truncation=True, max_length=TEXT_MAXLEN, return_tensors="pt")
    with torch.no_grad(): return torch.softmax(model(**enc).logits, -1).numpy().ravel()

def image_probs(pil):
    import torch
    m, tf = load_image()
    with torch.no_grad(): return torch.softmax(m(tf(pil.convert("RGB")).unsqueeze(0)), -1).numpy().ravel()

def show_topk(probs, true_code=None, k=3):
    for rank, i in enumerate(probs.argsort()[::-1][:k], 1):
        code = str(CLASS_ORDER[i]); hit = " ✅" if true_code and int(code) == int(true_code) else ""
        st.markdown(f"**{rank}. {LABELS_EN.get(code, code)}** · `{code}`{hit}")
        st.progress(float(probs[i]), text=f"{probs[i]*100:.1f}% confidence")

# examples
def load_samples():
    p = os.path.join(SAMP, "samples.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []
samples = load_samples()
st.markdown("#### Try a real Rakuten product — click one")
if samples:
    cols = st.columns(4)
    for i, s in enumerate(samples):
        with cols[i % 4]:
            ip = os.path.join(SAMP, s["image"])
            if os.path.exists(ip): st.image(ip, use_container_width=True)
            if st.button(s["name"], key=f"ex{i}", use_container_width=True):
                st.session_state.title_in, st.session_state.desc_in, st.session_state.ex = s["title"], s["description"], s
                st.rerun()
ex = st.session_state.get("ex")

title = st.text_input("Product title (French)", key="title_in", placeholder="e.g. Robot de piscine électrique Dolphin E10")
desc = st.text_area("Description (optional)", key="desc_in", height=80)
up = st.file_uploader("Or upload a product image", type=["jpg", "jpeg", "png"])

if st.button("Classify", type="primary"):
    if not TEXT_READY:
        st.warning("The CamemBERT model isn't in models/ yet — add it (CHECKLIST.md) and deploy on HF Spaces.")
    else:
        from PIL import Image
        text = (title + " " + desc).strip(); pil = None
        if up is not None: pil = Image.open(up); st.image(pil, width=220)
        elif ex and os.path.exists(os.path.join(SAMP, ex["image"])): pil = Image.open(os.path.join(SAMP, ex["image"]))
        tp = text_probs(text) if text else None
        ipx = image_probs(pil) if (pil is not None and IMG_READY) else None
        tc = ex["code"] if ex else None
        if tp is not None and ipx is not None:
            st.subheader("Prediction — Text + Image (fusion)"); show_topk((1-IMAGE_WEIGHT)*tp + IMAGE_WEIGHT*ipx, tc)
        elif tp is not None:
            st.subheader("Prediction — Text"); show_topk(tp, tc)
        elif ipx is not None:
            st.subheader("Prediction — Image only"); show_topk(ipx, tc)
        else: st.warning("Enter a title/description and/or upload an image.")
        if ex: st.caption(f"True category (from the Rakuten dataset): **{ex['name']}** · `{ex['code']}`")
footer()
