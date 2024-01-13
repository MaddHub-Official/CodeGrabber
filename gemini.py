# gemini.py

import os
import google.generativeai as genai
from dotenv import load_dotenv


def get_token():
    token = None
    while token is None:
            print('This program requires a Google Gemini API token to you can obtain a free token at: https://ai.google.dev\n')
            token = input("Please Enter API Token:\n")
            if len(token) == 39:
                return token
            print('Invalid token entered...')

if not os.path.exists(f'credentials.env'):
    token = get_token()
    # os.putenv("GEMINI_API_TOKEN", token)
    print("\nThank you! generating a credentials file...\n")
    with open("credentials.env", "w") as f:
        f.write(f"GEMINI_API_TOKEN='{token}'")


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
