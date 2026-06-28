import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
from google import genai
import json

client = genai.Client(api_key=API_KEY)


def evaluate_answer(question, user_answer):

    prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Candidate Answer:
{user_answer}

Evaluate the answer.

Return ONLY valid JSON.

The JSON must look exactly like this:

{{
    "score": 0,
    "strengths": [],
    "missing_concepts": [],
    "suggestions": []
}}

Rules:
- score should be an integer from 0 to 10.
- strengths must be a list of strings.
- missing_concepts must be a list of strings.
- suggestions must be a list of strings.
- Return ONLY JSON.
- Do not use markdown.
- Do not explain anything.
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