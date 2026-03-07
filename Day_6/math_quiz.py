import random
import time
import math

# create the math  question 

def generate_question():

    numberOne = random.randint(1,10)
    numberTwo = random.randint(1,10)
    operator = random.choice(['+', '-','/','*'])
    if operator == '+':
        answer = numberOne + numberTwo
    elif operator == '/':
        answer = numberOne / numberTwo
    elif operator == '*':
        answer = numberOne * numberTwo
    else:
        answer = numberOne - numberTwo
    return f"{numberOne}  {operator}  {numberTwo}" , answer



# main quiz logic

def mathQuiz():
    rounds = int(input("Enter your preferred number of time!"))
    score  = 0
    timer = int(input("Enter your timer value "))


    print("\n---- welcome to math quiz----")
    print('---- We are going to set math question, provide the correct answers! ----')

    for i in range(rounds):
        question, correctAns = generate_question()
    

        print(f"\n Question {i+1}, {question}")

        start_time = time.time()
        userAnswer = float(input("Enter Your Ans: "))
        elapse_time = timer - start_time

        if elapse_time > timer:
            print("Time is up!")
            continue
        
        elif userAnswer == correctAns:
            print("correct!")
            score += 1
        else:
            print(f"Wrong! The correct ans is {correctAns}")
            



    print("\n----Game Over----")
    print(f"Your final score is {score}/{rounds}")

    if score == rounds:
        print("Congratulations You Got all Right")
    elif score >= rounds // 2 :
        print("Well done you did well")
    else:
        print("keep on practicing to improve your math level")

mathQuiz()

generate_question()


      



