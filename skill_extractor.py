from resume_parser import extract_resume_text

def extract_skills(pdf_path):

    resume_text = extract_resume_text(pdf_path)

    skills_database = [
        "python",
        "machine learning",
        "tensorflow",
        "nlp",
        "pandas",
        "numpy",
        "sql",
        "java",
        "c++",
        "deep learning",
        "flask",
        "django",
        "pytorch",
        "opencv",
        "git"
    ]

    found_skills = []

    for skill in skills_database:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    return found_skills