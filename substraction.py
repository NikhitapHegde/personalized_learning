# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:10:13 2023

@author: poorn
"""

import csv
import random

math_score = 10
progress = 0
max_attempts = 5
start_index=[0,12,12,62,102,500,1101,8001,9001,10001]
end_index=[11,61,101,101,500,1100,8000,9000,10000,12000]
x=62
y=101

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

def evaluate_answer(user_answer, correct_answer):
    global progress, math_score
    if user_answer == correct_answer:
        print("YESS!! You are right!!")
        math_score += 1
        progress += 1
        return True
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
    return int(input("----"))

def main():
    global progress, math_score
    temp = 0
    while progress < 5:
        temp += 1
        current_question = get_question()
        attempts = 0

        while attempts < max_attempts:
            user_answer = ask_question(current_question)
            if evaluate_answer(user_answer,int( current_question[3])):
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

    print("Your math score:", math_score, "!!!")

# Load questions from the CSV file
with open(  "C:\\Users\poorn\Downloads\maths3 (1).csv", 'r') as source:
    questions = []
    for row in csv.reader(source):
        questions.append(row);

# Run the main function
main()
