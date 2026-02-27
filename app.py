import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

MODEL_PATH = "models/disease_model.keras"
CLASS_PATH = "models/class_indices.json"

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# Load correct class mapping
with open(CLASS_PATH, "r") as f:
    class_indices = json.load(f)

# Reverse dictionary: index -> class name
class_names = {v: k for k, v in class_indices.items()}

st.set_page_config(page_title="AI Plant Disease Detection", page_icon="🌿")

st.title("🌿 AI Plant Disease Detection")
st.caption("Upload a plant leaf image to detect disease")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:

    # Load image
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((224, 224))

    st.image(img, caption="Uploaded Image", use_container_width=True)

    # IMPORTANT: Match training preprocessing
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100

    # Get correct disease name
    disease_name = class_names[predicted_index]

    # Clean formatting
    disease_name = disease_name.replace("___", " - ").replace("_", " ")

    # Display
    st.success(f"🌿 Disease Detected: {disease_name}")
    st.info(f"Confidence: {confidence:.2f}%")