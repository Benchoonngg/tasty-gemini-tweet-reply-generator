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

def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # gemini-2.0-flash-exp
    generation_config=generation_config,
)

# Upload images
files = [
    upload_to_gemini("/Volumes/Hocson - External Device/Dump - External/994b571084e018fc70c5290f7316181d.jpg", mime_type="image/png"),
    upload_to_gemini("/Volumes/Hocson - External Device/Dump - External/6d30a47c4cba123611cb6d2f82150db9.jpg", mime_type="image/png"),
]

# Generate and print response
try:
    response = generate_creative_content(model)
    print("\nGenerated Responses:")
    print("-------------------")
    print(response.text)
    print("\nUsing Generation Config:")
    print("----------------------")
    for key, value in generation_config.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"Error generating content: {e}")