question=["What is the longest man-made structure in the world?",
    " Which region is known as the global center of technology?",
     "How many continents are there in the world?",
    " Which planet is known as the Red Planet?",
    " Who wrote the national anthem of India?",
    "Who invented the electric bulb?",
   "  What is the chemical symbol for water?",
     "How many players are there in a cricket team?",
    " Who painted the Mona Lisa?",
     "What is the currency of Japan?"]

answer=["Great Wall of China",
"Silicon Valley",
"7",
"Mars",
"Rabindranath Tagore",
"Thomas Edison",
"H2O",
"11",
"Leonardo da Vinci",
"Yen"]

score=0

print("""HI! LET PLAY A QUIZ
=======================""")
name=input("enter your name")

print("Q1:",question[0])
first=input("answer:")
if first.lower()==answer[0].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[0].lower())
    
print("Q2:",question[1])
second=input("answer:")
if second.lower()==answer[1].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[1].lower())
    
print("Q3:",question[2])
third=input("answer:")
if third.lower()==answer[2].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[2].lower())
    
print("Q4:",question[3])
forth=input("answer:")
if forth.lower()==answer[3].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[3].lower())
    
print("Q5:",question[4])
fifth=input("answer:")
if fifth.lower()==answer[4].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[4].lower())
    
print("Q6:",question[5])
sixth=input("answer:")
if sixth.lower()==answer[5].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[5].lower())
    
print("Q7:",question[6])
seventh=input("answer:")
if seventh.lower()==answer[6].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[6].lower())
    
print("Q8:",question[7])
eighth=input("answer:")
if eighth.lower()==answer[7].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[7].lower())
    
print("Q9:",question[8])
ninth=input("answer:")
if ninth.lower()==answer[8].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[8].lower())
    
print("Q10:",question[9])
tenth=input("answer:")
if tenth.lower()==answer[9].lower():
    print("correct")
    score=score+1
else:
    print("wrong! the correct answer is",answer[9].lower())
    print(f"congratulation {name} you have scored {score} mark out of 10")
    print("thank you")