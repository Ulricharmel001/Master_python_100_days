firstNum =  float(input("Enter the first number \n"))
secondNum = float(input("Enter the second number \n"))
thirdNum = float(input("Enter the third number \n"))

if firstNum > secondNum:
    print(f"first number {firstNum} is greater than second number {secondNum}")
elif secondNum == firstNum:
    print(f"SecondNum: {secondNum} is equal to firstNum {firstNum}")

else:
    print("invalid input ")

#challenge: compare 3 numbers, check if they are positive, include the option for user to run the
t#he peogram without restarting


while True:
    print("-----Welcome to Number comparison program----")
    firstNum =  float(input("Enter the first number \n"))
    secondNum = float(input("Enter the second number \n"))
    thirdNum = float(input("Enter the third number \n"))     
  
    


    checkType = [firstNum % 2, secondNum % 2, thirdNum % 2]

    print(checkType)

    if checkType[0] == 0 and checkType[1] == 0 and checkType[2] == 0 :
        print(" All three numbers are even number ")
        print([f"first Number : {firstNum}, Second Number : {secondNum} Third Number : {thirdNum}"])
        startAgain = input("Do you want to continue ? ( yes / no )").lower()
        if startAgain == "yes":
            continue
        else:
            break
    elif checkType[0] > 0 and checkType[1] > 0 and checkType[2] > 0 :
        print(" All number enter are odd number ")
        print(f" first number: {firstNum}, second Number : {secondNum}, third Number: {thirdNum}")
        startAgain = input("Do you want to continue ? ( yes / no )").lower()
        if startAgain == "yes":
            continue
        else:
            break
    else:
        print("it contain both even and odd number ")
        print(f"first Number: {firstNum}, second Number : {secondNum}, third Number: {thirdNum}")
        startAgain = input("Do you want to continue ? ( yes / no )").lower()
        if startAgain == "yes":
            continue
        else:
            break
