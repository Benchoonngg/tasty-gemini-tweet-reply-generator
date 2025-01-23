import os
import streamlit as st
import google.generativeai as genai
from config.generation_config import generation_config
from config.api_config import load_model, load_environment
from src.process_image_upload import process_uploaded_image  # ✅ Correct import
from src.generate_content import generate_creative_content

# Initialize Streamlit app
st.title("Tweet Reply Generator")
st.write("Upload an image, and we'll generate a tweet reply for it.")

# Load the model
api_key = load_environment()
model = load_model()

# File uploader for image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Generate Reply"):
        response = process_uploaded_image(model, uploaded_file)  # ✅ Use correct function
        
        if response:
            st.subheader("Generated Reply:")
            st.write(response)
