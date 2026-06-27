from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_questions(skills):

    prompt = f"""
You are an expert technical interviewer.

Generate interview questions based on these skills:

{', '.join(skills)}

Rules:
- Generate 2 questions per skill.
- Start with easy questions, then medium.
- Return ONLY valid JSON.

Format:

[
    {{
        "skill": "Python",
        "question": "What is Python?"
    }},
    {{
        "skill": "Python",
        "question": "What are decorators in Python?"
    }}
]
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").replace("```", "").strip()

    return json.loads(text)