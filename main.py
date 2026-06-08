from questions import questions 
question = list(questions.keys())[0]
print("Question:", question)
keywords = questions[question]
score =0
answer = input("your answer:")
print("Feedback:")
for i in keywords:
    if i.lower() in answer.lower():
        score +=1
print(f"score: {score}/{len(keywords)}") 





























