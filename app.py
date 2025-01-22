import os
import google.generativeai as genai
from config.generation_config import generation_config  # Add this import
from src.generate_content import generate_creative_content
from config.api_config import load_model, load_environment
from src.process_image_upload import upload_image

# Load the model
api_key = load_environment()  # Get API key from config
model = load_model()

upload_image(model)






