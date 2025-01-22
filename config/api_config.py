import os
import google.generativeai as genai
from dotenv import load_dotenv
from config.generation_config import generation_config

def load_model():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    return model  # Return the model instance

# Load and configure API
def load_environment():
    load_dotenv()   
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API Key not found! Check your .env file.")
    print("API Key Loaded:", api_key[:5] + "*****")  # Mask for security

    genai.configure(api_key=api_key)

    return api_key
