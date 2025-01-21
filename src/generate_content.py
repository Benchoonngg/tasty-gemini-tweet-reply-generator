import google.generativeai as genai
import json
import os
from typing import Union

def load_prompts(jsonl_path: str) -> list:
    """Load prompts from a JSONL file (line by line)."""
    prompts = []
    with open(jsonl_path, "r", encoding="utf-8") as file:
        for line in file:
            prompts.append(json.loads(line.strip()))
    return prompts

def generate_creative_content(model: genai.GenerativeModel) -> Union[str, genai.types.GenerateContentResponse]:
    """
    Generate creative content using the Gemini model.

    Args:
        model (genai.GenerativeModel): The initialized Gemini model
        
    Returns:
        Union[str, genai.types.GenerateContentResponse]: The model's response text or object
        
    Raises:
        Exception: If content generation fails
    """
    try:
        prompts_data = load_prompts("config/prompts.jsonl")

        # Extract instruction separately
        instruction = prompts_data[0]["instruction"]

        # Convert to Gemini format
        prompts = [instruction]
        for example in prompts_data[1:]:  # Skip first line (instruction)
            prompts.append(f"input {example['input']}")
            prompts.append(f"output {example['output']}")

        response = model.generate_content(prompts)
        return response

    except Exception as e:
        raise Exception(f"Failed to generate content: {e}")