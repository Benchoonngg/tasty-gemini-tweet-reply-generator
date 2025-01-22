import os
import google.generativeai as genai
from config.generation_config import generation_config
from src.generate_content import generate_creative_content

def upload_image(model):
    while True:
        image_path = input("Enter image path (or press Enter to finish): ")
        if not image_path:
            break
        if not os.path.exists(image_path):
            print("File not found. Try again.")
            continue
        
        try:
            uploaded_image = genai.upload_file(path=image_path, mime_type="image/jpeg")
            
            # Generate and print response for each uploaded image separately
            response = generate_creative_content(model, [uploaded_image])
            print("\nGenerated Response for:", image_path)
            print("-------------------")
            print(response.text)
            print("\nUsing Generation Config:")
            print("----------------------")
            for key, value in generation_config.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
