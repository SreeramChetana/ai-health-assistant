import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class HealthChatbot:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

        self.system_prompt = """
You are a helpful personal health assistant.

Rules:
- Provide general health information only
- Do NOT give medical diagnosis
- Do NOT prescribe medicines
- Always suggest consulting a doctor for serious issues
- Keep answers simple and safe
"""

    def ask(self, user_query):
        prompt = self.system_prompt + "\nUser: " + user_query

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text