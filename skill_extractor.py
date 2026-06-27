from resume_parser import extract_resume_text

def extract_skills():

    resume_text = extract_resume_text(
        r"C:\Users\aseen\Downloads\Resume_test.pdf"
    )

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

    print("\nSkills Found:")
    for skill in found_skills:
        print("✓", skill)

    return found_skills