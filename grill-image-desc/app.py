import streamlit as st
import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

st.title("🖼️ Image Description with Amazon Nova (OpenRouter)")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Describe Image"):
        img_bytes = uploaded_file.read()
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")

        url = "https://openrouter.ai/api/v1/chat/completions"

        payload = {
            "model": "amazon/nova-2-lite-v1:free",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Please describe what you see in this image including objects, context, and details."},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{img_b64}"}
                    ]
                }
            ]
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        with st.spinner("Generating description..."):
            response = requests.post(url, json=payload, headers=headers)
            result = response.json()

            description = result["choices"][0]["message"]["content"]

            st.success("Description Generated!")
            st.write(description)
