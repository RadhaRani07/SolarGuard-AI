import json
import gdown
import os
import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

st.set_page_config(
    page_title="SolarGuard AI",
    page_icon="☀️"
)

st.title("SolarGuard AI")
st.write("AI-Based Solar Panel Condition Classification")

# Load class names
with open("class_names.json", "r") as file:
    class_names = json.load(file)

# Select device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Download model from Google Drive if it is not available
model_path = "solarguard_experiment2.pth"
file_id = "1UbpkDQ-Vbu3NoNjNwW3oWvgW22G1nnem"

if not os.path.exists(model_path):
    with st.spinner("Downloading trained AI model..."):
        gdown.download(
            f"https://drive.google.com/uc?id={file_id}",
            model_path,
            quiet=False
        )

if not os.path.exists(model_path) or os.path.getsize(model_path) == 0:
    st.error("Model download failed. Check Google Drive sharing permissions.")
    st.stop()

# Load trained model
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, len(class_names))

model.load_state_dict(
    torch.load(model_path, map_location=device)
)

model = model.to(device)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Upload image
uploaded_file = st.file_uploader(
    "Upload a solar panel image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Solar Panel",
        use_container_width=True
    )

    if st.button("Predict Condition"):
        image_tensor = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(image_tensor)
            probabilities = torch.softmax(outputs, dim=1)[0]

        predicted_index = probabilities.argmax().item()
        predicted_class = class_names[predicted_index]
        confidence_value = probabilities[predicted_index].item() * 100

        st.subheader("Prediction Result")
        st.write("**Predicted Class:**", predicted_class)
        st.write(f"**Model Confidence:** {confidence_value:.2f}%")

        st.subheader("All Class Probabilities")

        for i, class_name in enumerate(class_names):
            probability = probabilities[i].item() * 100

            st.write(f"{class_name}: {probability:.2f}%")
            st.progress(probability / 100)

        st.warning(
            "Educational AI prototype only. Predictions are estimates, "
            "not confirmed diagnoses of solar panel condition."
        )
