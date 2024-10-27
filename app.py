import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit app title
st.title("Fireworks Image Generation")

# Input fields
api_key = st.text_input("API Key", os.getenv("API_KEY"), type="password")
prompt = st.text_input("Prompt", "generate a bangladeshi beautiful women pic")
aspect_ratio = st.selectbox("Aspect Ratio", ["16:9", "4:3", "1:1"])
guidance_scale = st.slider("Guidance Scale", 1.0, 10.0, 3.5)
num_inference_steps = st.slider("Number of Inference Steps", 1, 100, 30)

# Button to generate image
if st.button("Generate Image"):
    url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-dev-fp8/text_to_image"
    headers = {
        "Content-Type": "application/json",
        "Accept": "image/jpeg",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Generated Image")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
