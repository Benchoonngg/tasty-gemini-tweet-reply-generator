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
        prompts_data = load_prompts("config/prompts.jsonl")

        instructions = load_instructions("config/instructions.jsonl")

        # Extract instruction separately
        instruction = instructions[0]["instruction"]

        # Multi-instruction example
        instruction = instructions[1]["instruction"]
        instruction = instructions[2]["instruction"]

        # Convert to Gemini format, incorporating image URIs
        contents = [instruction]
        for example in prompts_data[1:]:  # Skip first line (instruction)
            contents.append(f"input {example['input']}")
            contents.extend(image_uris)  # Add all image URIs
            contents.append(f"output {example['output']}")

        response = model.generate_content(contents)
        return response

    except Exception as e:
        raise Exception(f"Failed to generate content: {e}")