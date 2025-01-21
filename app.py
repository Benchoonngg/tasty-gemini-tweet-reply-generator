import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.generate_content import generate_creative_content
from config.generation_config import generation_config

# Load and configure API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found! Check your .env file.")
print("API Key Loaded:", api_key[:5] + "*****")  # Mask for security
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Upload the images and get their URIs
image_files = [
    genai.upload_file(path="Tweet Reply Data/Main Post/image_1037.png", mime_type="image/jpeg"),
]

# Generate and print response
try:
    response = generate_creative_content(model, image_files)
    print("\nGenerated Responses:")
    print("-------------------")
    print(response.text)
    print("\nUsing Generation Config:")
    print("----------------------")
    for key, value in generation_config.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"Error generating content: {e}")