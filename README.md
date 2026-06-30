# Smart Interview Analyzer

Smart Interview Analyzer is an AI-powered interview simulation platform that analyzes a candidate's resume, generates personalized interview questions, and evaluates responses in real time using Google's Gemini API.

## Features

- Upload a resume in PDF format
- Extract and analyze resume content
- Generate interview questions based on the candidate's profile
- Evaluate answers using AI
- Provide strengths, missing concepts, and suggestions for improvement
- Interactive web interface built with Streamlit

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- pdfplumber
- Natural Language Processing (NLP)
- Large Language Models (LLMs)

## How It Works

1. Upload your resume.
2. The application extracts and analyzes the resume content.
3. Gemini generates interview questions based on your profile.
4. Answer the generated questions.
5. The AI evaluates your responses and provides:
   - Overall score
   - Strengths
   - Missing concepts
   - Suggestions for improvement

## Project Structure

```text
app.py                  # Main Streamlit application
resume_parser.py        # Resume parsing
question_generator.py   # Interview question generation
gemini_evaluator.py     # Answer evaluation
requirements.txt
README.md
```

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd smart-interview-analyzer
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

- Voice-based interview support
- Speech-to-text integration
- Follow-up questions based on previous answers
- Improved evaluation logic
- Performance dashboard
- Multi-round interview simulation

## Contributing

Suggestions and feedback are welcome. Feel free to open an issue or submit a pull request.

## Contact

If you'd like to discuss this project or connect regarding AI and Machine Learning, feel free to reach out on LinkedIn.