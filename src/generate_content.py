import google.generativeai as genai
import json
import os
from typing import Union, List

def load_prompts(jsonl_path: str) -> list:
    """Load prompts from a JSONL file (line by line)."""
    prompts = []
    with open(jsonl_path, "r", encoding="utf-8") as file:
        for line in file:
            prompts.append(json.loads(line.strip()))
    return prompts

def load_instructions(jsonl_path: str) -> list:
    """Load prompts from a JSONL file (line by line)."""
    prompts = []
    with open(jsonl_path, "r", encoding="utf-8") as file:
        for line in file:
            prompts.append(json.loads(line.strip()))
    return prompts

def generate_creative_content(model: genai.GenerativeModel, image_uris: List[str]) -> Union[str, genai.types.GenerateContentResponse]:
    """
    Generate creative content using the Gemini model, incorporating images.

    Args:
        model (genai.GenerativeModel): The initialized Gemini model.
        image_uris (List[str]): A list of URIs for the uploaded images.

    Returns:
        Union[str, genai.types.GenerateContentResponse]: The model's response text or object.

    Raises:
        Exception: If content generation fails.
    """
    try:
        # Load user config
        with open('config/user_config.json', 'r', encoding='utf-8') as file:
            user_config = json.load(file)

        prompts_data = load_prompts("config/prompts.jsonl")
        instruction = user_config['instruction']

        # Convert to Gemini format, incorporating image URIs
        contents = [instruction]
        for example in prompts_data:
            contents.append(f"input {example['input']}")
            contents.extend(image_uris)
            contents.append(f"output {example['output']}")

        # Debugging: Print the generation parameters
        print("Generation Parameters:", {
            "temperature": user_config['temperature'],
            "top_p": user_config['top_p'],
            "top_k": user_config['top_k']
        })

        # Use the model's method correctly with a single contents argument
        response = model.generate_content(contents)
        return response

    except Exception as e:
        raise Exception(f"Failed to generate content: {e}")