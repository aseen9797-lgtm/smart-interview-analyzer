from questions import questions 
t_score =0
t_key =0
for question, keywords in questions.items():
     print("Question:", question)
     keywords = questions[question]
     score =0
     answer = input("your answer:")
     print("Feedback:")
for i in keywords:
    if i.lower() in answer.lower():
        print("yes", i)
        score +=1
    else:
        print("no", i)
print(f"score: {score}/{len(keywords)}") 

t_score += score
t_key += len(keywords)

print("\nInterview Completed!")

print(f"Final Score: {t_score}/{t_key}")





























