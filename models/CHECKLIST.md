# Files needed to run the FULL fused model (drop into this folder)

## From Jonathan (text branch + fusion)
1. Fine-tuned CamemBERT — a folder `camembert/` from model.save_pretrained() + tokenizer.save_pretrained():
   config.json, model.safetensors (or pytorch_model.bin, ~450 MB), tokenizer.json /
   sentencepiece.bpe.model, tokenizer_config.json, special_tokens_map.json
2. class order: the 27 prdtypecodes in the model OUTPUT index order (LabelEncoder.classes_).
   Replace class_order.json if it differs from the default sorted order.
3. Fusion: method + image weight (default 0.30 in app.py). If a meta-classifier is used instead of
   weighted late fusion, send that model + a 2-line "how to combine" note.
4. Text preprocessing CamemBERT expects (raw vs cleaned text; max_length, default 256).

## From Thomas (image branch)
1. image_model.pth — a torch state_dict.
2. Architecture: which CNN (resnet18 / efficientnet_b0) -> set IMAGE_ARCH in app.py.
3. Image transforms: resize size (default 224) + normalization mean/std (default ImageNet).
4. Must output the SAME 27 classes in the SAME order as the text model (for fusion to align).

## Already provided (Sandeep)
- labels_en.json (code -> name), class_order.json (default; confirm/replace)
- TF-IDF vectorizer + feature matrix on Google Drive.
