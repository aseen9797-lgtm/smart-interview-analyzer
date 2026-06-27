from questions import questions
from skill_extractor import generate_questions
from gemini_evaluator import evaluate_answer
selected_questions, found_skills = generate_questions()
total_score = 0
report = []
category_scores = {}
for question in selected_questions:

    if question not in questions:
        continue

    category = questions[question]["category"]

    print("\nQuestion:", question)

    user_answer = input("Your answer: ")

    feedback = evaluate_answer(question, user_answer)

    score = feedback["score"]
    strengths = feedback["strengths"]
    missing = feedback["missing_concepts"]
    suggestions = feedback["suggestions"]

    print(f"\nScore: {score}/10")

    print("\nStrengths:")
    for item in strengths:
        print("✓", item)

    print("\nMissing Concepts:")
    for item in missing:
        print("✗", item)

    print("\nSuggestions:")
    for item in suggestions:
        print("→", item)

    total_score += score

    report.append({
        "question": question,
        "score": score,
        "strengths": strengths,
        "missing": missing,
        "suggestions": suggestions
    })

    if category not in category_scores:
        category_scores[category] = []

    category_scores[category].append(score)

if len(report) > 0:
    average_score = total_score / len(report)
else:
    average_score = 0

print("\nInterview Completed!")

print(f"\nAverage Score: {average_score:.2f}/10")

print("\nDetected Skills:")
for skill in found_skills:
    print("✓", skill)

print("\nCategory Performance:")
for category, scores in category_scores.items():
    avg = sum(scores) / len(scores)
    print(f"{category}: {avg:.2f}/10")

print("\nInterview Report")

for item in report:
    print("\n------------------------")
    print("Question:", item["question"])
    print(f"Score: {item['score']}/10")

    print("\nStrengths:")
    for s in item["strengths"]:
        print("✓", s)

    print("\nMissing Concepts:")
    for m in item["missing"]:
        print("✗", m)

    print("\nSuggestions:")
    for sug in item["suggestions"]:
        print("→", sug)

if average_score >= 8:
    print("\nExcellent performance!")

elif average_score >= 6:
    print("\nGood performance!")

else:
    print("\nNeeds improvement.")

with open("report.txt", "w", encoding="utf-8") as file:

    file.write("Interview Report\n")
    file.write("===========================\n\n")

    file.write(f"Average Score: {average_score:.2f}/10\n\n")

    file.write("Detected Skills:\n")
    for skill in found_skills:
        file.write(f"✓ {skill}\n")

    file.write("\nCategory Performance:\n")

    for category, scores in category_scores.items():
        avg = sum(scores) / len(scores)
        file.write(f"{category}: {avg:.2f}/10\n")

    file.write("\nDetailed Report\n")

    for item in report:

        file.write("\n---------------------------------\n")
        file.write(f"Question: {item['question']}\n")
        file.write(f"Score: {item['score']}/10\n\n")

        file.write("Strengths:\n")
        for s in item["strengths"]:
            file.write(f"✓ {s}\n")

        file.write("\nMissing Concepts:\n")
        for m in item["missing"]:
            file.write(f"✗ {m}\n")

        file.write("\nSuggestions:\n")
        for sug in item["suggestions"]:
            file.write(f"→ {sug}\n")

print("\nReport saved successfully to report.txt")
