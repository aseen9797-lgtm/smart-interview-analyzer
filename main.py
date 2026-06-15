ffrom questions import questions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def compare_answers(ideal_answer, user_answer):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([ideal_answer, user_answer])
    similarity = cosine_similarity(vectors[0], vectors[1])
    score = similarity[0][0] * 100
    return score
total_score = 0
for question, data in questions.items():
    print("\nQuestion:", question)
    user_answer = input("Your answer: ")
    ideal_answer = data["ideal_answer"]
    concepts = data["concepts"]
    score = compare_answers(ideal_answer, user_answer)
    print(f"Similarity Score: {score:.2f}%")
    print("\nMatched Concepts:")
    for concept in concepts:
        if concept.lower() in user_answer.lower():
            print("✓", concept)
    print("\nMissing Concepts:")
    for concept in concepts:
        if concept.lower() not in user_answer.lower():
            print("✗", concept)
    total_score += score
average_score = total_score / len(questions)
print("\nInterview Completed!")
print(f"Average Score: {average_score:.2f}%")
if average_score >= 80:
    print("Excellent performance!")
elif average_score >= 60:
    print("Good performance!")
else:
    print("Needs improvement.")