import os
import streamlit as st
import google.generativeai as genai
from config.static.generation_config import generation_config
from config.static.api_config import load_model, load_environment
from src.process_image_upload import process_uploaded_image  # ✅ Correct import
from src.generate_content import generate_creative_content
import json

# Initialize Streamlit app
st.title("Tweet Reply Generator")
st.write("Upload the MAIN POST to generate a tweet reply.")

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

# Load user config
def load_user_config():
    with open('config/user_config.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Save user config
def save_user_config(config):
    with open('config/user_config.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4)

# Streamlit UI
st.title("User Configuration Editor")

# Load current config
user_config = load_user_config()

# Instruction Editor
st.subheader("Edit Instruction")
new_instruction = st.text_area("Instruction", value=user_config['instruction'])
if st.button("Save Instruction"):
    user_config['instruction'] = new_instruction
    save_user_config(user_config)
    st.success("Instruction updated successfully!")

# Generation Config Editor
st.subheader("Edit Generation Config")
temperature = st.slider("Temperature", 0, 2, user_config['temperature'])
top_p = st.slider("Top P", 0.0, 1.0, user_config['top_p'])
top_k = st.slider("Top K", 0, 100, user_config['top_k'])

if st.button("Save Generation Config"):
    user_config.update({"temperature": temperature, "top_p": top_p, "top_k": top_k})
    save_user_config(user_config)
    st.success("Generation config updated successfully!")