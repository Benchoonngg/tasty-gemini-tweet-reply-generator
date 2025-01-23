import os
import tempfile
import google.generativeai as genai
from config.generation_config import generation_config
from src.generate_content import generate_creative_content

def process_uploaded_image(model, uploaded_file):
    try:
        # Create a temporary file to save the uploaded image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.getbuffer())  # Write the uploaded file to the temp file
            temp_file_path = temp_file.name  # Get the path of the temp file

        # Upload the temporary file
        uploaded_image = genai.upload_file(path=temp_file_path, mime_type=uploaded_file.type)

        # Generate the response using the uploaded image
        response = generate_creative_content(model, [uploaded_image])
        return response.text

    except Exception as e:
        return f"Error processing image: {e}"
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)