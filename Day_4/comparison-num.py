firstNum =  float(input("Enter the first number \n"))
secondNum = float(input("Enter the second number \n"))
thirdNum = float(input("Enter the third number \n"))

if firstNum > secondNum:
    print(f"first number {firstNum} is greater than second number {secondNum}")
elif secondNum == firstNum:
    print(f"SecondNum: {secondNum} is equal to firstNum {firstNum}")

else:
    print("invalid input ")

# challenge: compare 3 numbers, check if they are positive, include the option for user to run the
# the peogram without restarting
    