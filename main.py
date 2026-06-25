from questions import questions
from skill_extractor import generate_questions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare_answers(ideal_answer, user_answer):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([ideal_answer, user_answer])
    similarity = cosine_similarity(vectors[0], vectors[1])
    score = similarity[0][0] * 100
    return score

selected_questions = generate_questions()

total_score = 0
report = []
category_scores = {}

for question in selected_questions:

    if question not in questions:
        continue

    data = questions[question]

    print("\nQuestion:", question)

    matched = []
    missing = []

    user_answer = input("Your answer: ")

    ideal_answer = data["ideal_answer"]
    concepts = data["concepts"]
    category = data["category"]

    score = compare_answers(ideal_answer, user_answer)

    print(f"Similarity Score: {score:.2f}%")

    print("\nMatched Concepts:")
    for concept in concepts:
        if concept.lower() in user_answer.lower():
            print("✓", concept)
            matched.append(concept)

    print("\nMissing Concepts:")
    for concept in concepts:
        if concept.lower() not in user_answer.lower():
            print("✗", concept)
            missing.append(concept)
    total_score += score
    report.append({
        "question": question,
        "score": score,
        "matched": matched,
        "missing": missing
    })
    if category not in category_scores:
        category_scores[category] = []

    category_scores[category].append(score)
if len(report) > 0:
    average_score = total_score / len(report)
else:
    average_score = 0
print("\nInterview Completed!")
print(f"Average Score: {average_score:.2f}%")
print("\nCategory Performance:")
for category, scores in category_scores.items():
    avg = sum(scores) / len(scores)
    print(f"{category}: {avg:.2f}%")
print("\nInterview Report")
for item in report:
    print("-------------------")
    print("Question:", item["question"])
    print(f"Score: {item['score']:.2f}%")
    print("Matched Concepts:")
    for concept in item["matched"]:
        print("✓", concept)
    print("Missing Concepts:")
    for concept in item["missing"]:
        print("✗", concept)
if average_score >= 80:
    print("\nExcellent performance!")
elif average_score >= 60:
    print("\nGood performance!")
else:
    print("\nNeeds improvement.")