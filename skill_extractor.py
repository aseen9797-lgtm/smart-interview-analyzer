from questions_mapping import skill_mapping
import random
def generate_questions():
   from resume_parser import extract_resume_text

resume_text = extract_resume_text(
    r"C:\Users\aseen\Downloads\Resume_test.pdf"
)
    found_skills = []
    for skill in skill_mapping:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)
    print("\nSkills Found:")
    for skill in found_skills:
        print("✓", skill)
    print("\nGenerated Questions:")
    generated_questions = []
    for skill in found_skills:
        question = random.choice(skill_mapping[skill])
        generated_questions.append(question)
        print("-", question)
    generated_questions = list(set(generated_questions))
return generated_questions, found_skills