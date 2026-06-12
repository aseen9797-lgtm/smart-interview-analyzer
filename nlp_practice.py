#t = input("enter ur sentence :")
#s = t.split()
#print(s)
# this is tokenization in nlp 

"""text = input("Enter a sentence: ")
words = text.split()
print(words)
print("Number of words:", len(words))"""

# normalization in nlp

"""t = input("enter sentence: ")
t1 = t.lower()
t2 = t1.split()
print(t2)"""

#checking if nltk library is downloaded or not
"""import nltk
print("yes")"""

#now lets do stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["prediction" ,"predicted","predicting","predict"]
for i in words:
    print(i, stemmer.stem(i))
