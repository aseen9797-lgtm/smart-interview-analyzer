from google import genai
import streamlit as st
import json

API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)


def generate_questions(skills):

    prompt = f"""
You are a strict JSON generator.

Generate interview questions.

Skills: {', '.join(skills)}

Rules:
- 2 questions per skill
- easy to medium difficulty
- ONLY return valid JSON array
- NO markdown, NO explanation

Format:
[
  {{"skill": "Python", "question": "..."}},
  {{"skill": "Python", "question": "..."}}
]
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        text = response.text.strip()
        text = text.replace("```json", "").replace("```", "").strip()

        questions = json.loads(text)

        if not isinstance(questions, list):
            raise ValueError("Invalid format")

        return questions

    except Exception as e:
        st.error("Failed to generate questions. Please retry.")
        st.write(str(e))
        return []