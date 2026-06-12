from questions import questions
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def clean_text(answer):
    t1 = answer.lower()
    t2 = t1.split()
    stop_words = ["is", "a","the","an", "and","to","in","of","are","for"]
    filtered =[]
    for j in t2:
        if j not in stop_words:
            filtered.append(stemmer.stem(j))
    return filtered
t_score = 0
t_key = 0
for question, keywords in questions.items():
    print("\nQuestion:", question)
    score = 0
    answer = input("Your answer: ")
    filtered = clean_text(answer)
    print("Feedback:")
    for i in keywords:
        if stemmer.stem(i.lower()) in filtered:
            print("yes", i)
            score += 1
        else:
            print("no", i)
    print(f"Score: {score}/{len(keywords)}")
    t_score += score
    t_key += len(keywords)
print("\nInterview Completed!")
print(f"Final Score: {t_score}/{t_key}")
percentage = (t_score / t_key) * 100

print(f"\nFinal Score: {t_score}/{t_key}")
print(f"Percentage: {percentage:.2f}%")
if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 60:
    print("Good performance!")
else:
    print("Needs improvement.")