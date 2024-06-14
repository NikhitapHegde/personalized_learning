# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:37:43 2023

@author: poorn
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:33:17 2023

@author: poorn
"""

import csv
import random

math_score = 0
progress = 0
max_attempts = 5
start_index=[1,12,121,522,1422,2943,5000,10001,100001]
end_index=[11,120,521,1421,2942,5000,10000,100000,800000]
x=0
y=0
def get_index_range(age):
    global x,y
    if age == 6:
        x=1
        y=12
    elif age in [7, 8]:
        x= 12
        y=121
    elif age in [9, 10]:
        x=121
        y=522
    elif age in [11, 12]:
        x= 121
        y=522
    

def get_question():
    global x,y,progress
    if(progress>=4):
        progress=0
        print("Try solving tougher questions")
        print()
        temp=start_index.index(x)
        x=start_index[temp+1]
        y=end_index[temp+1]
    elif(progress<0):
        print("Try solving easier questions")
        print()
        temp=start_index.index(x)
        if(temp!=0):
            x=start_index[temp-1]
            y=end_index[temp-1]       
    return random.choice(questions[x:y])


def evaluate_answer(user_answer, correct_answer,math_score):
    global progress
    if user_answer == correct_answer:
        print("YESS!! You are right!!")
        math_score += 1
        progress += 1
        return math_score
    elif user_answer == correct_answer - 1 or user_answer == correct_answer + 1:
        print("It's not exactly correct :( You are almost close. Try again.")
        progress = 0
        return False
    else:
        print("It's a wrong answer :(")
        progress=0
        return False

def ask_question(question):
    print("What is the difference of", question[0], "and", question[1], "?")
    print("Enter your answer, or type 'quit' to exit.")
    user_input = input("----")
    
    if user_input.isalpha():
        if user_input.lower() == 'quit':
            #print("You chose to quit. Exiting the program.")
            return (user_input.lower())

    return int(user_input)

def main(math_score,age):
    global progress
    math_score=int(math_score)
    get_index_range(age)
    temp = 0
    while progress < 5:
        temp += 1
        current_question = get_question()
        attempts = 0

        while attempts < max_attempts:
            user_answer = ask_question(current_question)
            if user_answer == 'quit':
                print("Your substraction score:", math_score, "!!!")
                return math_score
            
            p= evaluate_answer(user_answer,int( current_question[3]),math_score)
            if(p):
                math_score=p
                break
            else:
                attempts += 1

        if attempts == max_attempts:
            progress=-1
            print("You reached the maximum attempts for this question. The correct answer is:", current_question[2])

        

        if temp == 3 and progress == 3:
            print("3 consecutive correct answers!! Extra score.")
            print()
            math_score += 1
            temp = 0

    

# Load questions from the CSV file
with open(  "C:\Users\user\Downloads\mathss1.csv", 'r') as source:
    questions = []
    for row in csv.reader(source):
        questions.append(row);

# Run the main function
#main()
