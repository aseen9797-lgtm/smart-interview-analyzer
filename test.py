from gemini_evaluator import evaluate_answer

result = evaluate_answer(
    "What is Python?",
    "Python is a programming language."
)

print(result)

print(result["score"])

print(result["strengths"])

print(result["missing_concepts"])

print(result["suggestions"])