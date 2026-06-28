import streamlit as st
import tempfile

from skill_extractor import extract_skills
from question_generator import generate_questions
from gemini_evaluator import evaluate_answer

st.set_page_config(
    page_title="AI Interviewer",
    page_icon="🤖"
)

st.title("🤖 Smart Interview Analyzer")

st.write("Upload your resume to begin your AI interview.")

# ----------------------------
# Initialize session state
# ----------------------------
if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_q" not in st.session_state:
    st.session_state.current_q = 0

if "scores" not in st.session_state:
    st.session_state.scores = []

if "started" not in st.session_state:
    st.session_state.started = False

# ----------------------------
# Upload Resume
# ----------------------------
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    # Analyze button
    if st.button("Start Interview"):

        with st.spinner("Analyzing resume..."):

            skills = extract_skills(pdf_path)
            questions = generate_questions(skills)

            st.session_state.questions = questions
            st.session_state.started = True
            st.session_state.current_q = 0
            st.session_state.scores = []

        st.success("Interview Started!")

# ----------------------------
# Interview Flow
# ----------------------------
if st.session_state.started and len(st.session_state.questions) > 0:

    q_index = st.session_state.current_q
    questions = st.session_state.questions

    if q_index < len(questions):

        question = questions[q_index]

        st.subheader(f"Question {q_index + 1}")
        st.write(question["question"])

        user_answer = st.text_area("Your Answer", key=f"answer_{q_index}")

        if st.button("Submit Answer", key=f"submit_{q_index}"):

            if user_answer.strip() == "":
                st.warning("Please enter an answer first!")
            else:

                feedback = evaluate_answer(
                    question["question"],
                    user_answer
                )

                st.success(f"Score: {feedback['score']}/10")

                st.write("### Strengths")
                for s in feedback["strengths"]:
                    st.write("✅", s)

                st.write("### Missing Concepts")
                for m in feedback["missing_concepts"]:
                    st.write("❌", m)

                st.write("### Suggestions")
                for sug in feedback["suggestions"]:
                    st.write("➡️", sug)

                # Save score
                st.session_state.scores.append(feedback["score"])

                # Next question button
                if st.button("Next Question"):
                    st.session_state.current_q += 1
                    st.rerun()

    else:
        # Final results
        st.subheader("🎯 Interview Completed!")

        avg_score = sum(st.session_state.scores) / len(st.session_state.scores)

        st.write(f"### Final Score: {avg_score:.2f}/10")

        if avg_score >= 8:
            st.success("Excellent Performance 🔥")
        elif avg_score >= 6:
            st.info("Good Performance 👍")
        else:
            st.warning("Needs Improvement 📚")

        st.write("### All Scores")
        st.write(st.session_state.scores)