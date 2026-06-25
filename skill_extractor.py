from questions_mapping import skill_mapping
import random
def generate_questions():
    resume_text = input("Paste your resume:\n")
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
    return generated_questions  
