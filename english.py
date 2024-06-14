import csv
import random

eng_score = 0
progress = 0
max_attempts = 5
start_index=[0,26,58,91]
end_index=[25,56,88,144]

x=0
y=25

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

def evaluate_answer(user_answer, correct_answer,eng_score):
    global progress
    if user_answer.lower() == correct_answer.lower():
        print("YESS!! You are right!!")
        eng_score += 1
        progress += 1
        return eng_score
    
    else:
        print("It's a wrong answer :(")
        progress=0
        return False

def ask_question(question):
    print("Rearrage the letters to form meaning full words", question[0])
    print("Enter your answer, or type 'quit' to exit.")
    user_input = input("----")
    
    if user_input.isalpha():
        if user_input.lower() == 'quit':
            print("You chose to quit. Exiting the program.")
            return (user_input.lower())

    return user_input

def main(eng_score,age):
    global progress
    temp = 0
    while progress < 5:
        temp += 1
        current_question = get_question()
        attempts = 0

        while attempts < max_attempts:
            user_answer = ask_question(current_question)
            if user_answer == 'quit':
                print("Your eng score:", eng_score, "!!!")
                return eng_score
            
            p= evaluate_answer(user_answer, current_question[1],eng_score)
            if(p):
                eng_score=p
                break
            else:
                attempts += 1

        if attempts == max_attempts:
            progress=-1
            print("You reached the maximum attempts for this question. The correct answer is:", current_question[2])

        

        if temp == 3 and progress == 3:
            print("3 consecutive correct answers!! Extra score.")
            print()
            eng_score += 1
            temp = 0

    

# Load questions from the CSV file
with open(  "C:\Users\user\Downloads\Ai project.zip\Ai project\english.csv", 'r') as source:
    questions = []
    for row in csv.reader(source):
        questions.append(row);

# Run the main function
main(10,5)
