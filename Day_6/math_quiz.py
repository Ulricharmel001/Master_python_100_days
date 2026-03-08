import random
import time
import math
import threading
import sys


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


def input_with_timeout(prompt, timeout):
    """Get user input with timeout. Returns (answer, timed_out) tuple."""
    result = [None]
    timed_out = [False]
    
    def get_input():
        try:
            result[0] = input(prompt)
        except:
            pass
    
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(timeout)
    
    if input_thread.is_alive():
        timed_out[0] = True
        print("\nTime's up!")
        return None, True
    
    return result[0], False



# main quiz logic

def mathQuiz():
    rounds = int(input("Enter your preferred number of questions!\n"))
    score  = 0
    timer = int(input("Enter your timer value\n")) 


    print("\n---- welcome to math quiz----")
    print('---- We are going to set math question, provide the correct answers! ----')

    for i in range(rounds):
        question, correctAns = generate_question()


        print(f"\n Question {i+1}, {question}")

        userAnswer, timed_out = input_with_timeout("Your answer: ", timer)

        if timed_out:
            print(f"The correct answer was {correctAns}")
            continue

        elif userAnswer == str(correctAns):
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


      



