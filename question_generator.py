from google import genai
import streamlit as st
import json

# Get API key from Streamlit secrets (NOT dotenv)
API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)
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
        model="gemini-1.5-flash",
        contents=prompt
    )
    text = response.text.strip()
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)