# Smart Interview Analyzer

An AI-powered interview simulator that analyzes a candidate's resume, generates personalized interview questions, and evaluates responses in real time using Google's Gemini API.

## Overview

Smart Interview Analyzer is designed to simulate a personalized technical interview. Instead of asking generic questions, the application analyzes the uploaded resume and generates interview questions tailored to the candidate's skills, projects, and experience.

The project explores how Large Language Models (LLMs) and Natural Language Processing (NLP) can be applied to interview preparation and hiring workflows.

## Features

- Upload a resume in PDF format
- Resume parsing using pdfplumber
- AI-generated interview questions based on resume content
- Real-time answer evaluation
- Feedback including:
  - Overall score
  - Strengths
  - Missing concepts
  - Suggestions for improvement
- Interactive web interface built with Streamlit

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- pdfplumber
- Natural Language Processing (NLP)
- Large Language Models (LLMs)

## Project Workflow

1. Upload a resume.
2. The application extracts and analyzes the resume.
3. Gemini generates personalized interview questions.
4. The candidate answers the questions.
5. The AI evaluates each response and provides constructive feedback.

## Installation

```bash
git clone https://github.com/aseen9797-lgtm/smart-interview-analyzer.git

cd smart-interview-analyzer

pip install -r requirements.txt

streamlit run app.py
```

## Future Improvements

- Voice-based interviews
- Speech-to-text integration
- Follow-up questions based on previous responses
- Improved scoring and evaluation logic
- Multi-round interview simulation
- Performance analytics dashboard

## Author

Aseen

Feel free to connect with me on LinkedIn or share suggestions for improving the project.