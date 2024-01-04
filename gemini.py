import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv('credentials.env')

genai.configure(api_key=os.getenv('GEMINI_API_TOKEN'))


class Generator:

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

    safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                        generation_config=generation_config,
                                        safety_settings=safety_settings)

    def prompt(self, game_name=str):
        prompt_parts = [
            f"Find Roblox codes for the game: {game_name}.",
        ]
        response = self.model.generate_content(prompt_parts)
        return response.text

