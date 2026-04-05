FILE = "Error.txt"

def add(x, y):
    return x + y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
def substract(x,y):
    return x - y

def modular(x,y):
    return x // y

def raiseToPower(x,y):
    return x**y

def showMenu():
    print("---- Safe Calculator----")
    print("1. Add")
    print("2. Divide")
    print("3. Multiply")
    print("4. Substract")
    print("5. Modular division")
    print("6. Raise to the power")
    print("7. Exit")


while True:
    showMenu()
    choice = input(" Enter your choice !")
    if choice == "7":
            print("Thank you for using safe calculator")
            print("Bye!")
            break
    

    try:
        x = int(input("Enter the first number!"))
        y = int(input("Enter the second number!"))
        if choice == "1":
            print("Result: " , add(x, y))
        elif choice == "2":
            print("Result: ", divide(x, y))
        elif choice == "3":
            print("Result :",  multiply(x, y))
        elif choice == "4":
            print("Result: ", substract(x, y))
        elif choice == "5":
            print("Result :", modular(x,y))
        elif choice == "6":
            print("Result: ",    raiseToPower(x, y))
       
        with open(FILE, 'a') as file:
           file.write(f"Error: Invalid Value {e} \n")
        print("Error : Invalid input ")
    except ZeroDivisionError as e:
        with open(FILE, "a") as file:
            file.write(f"Error: Cannot divide by zero {e}\n" )
        print(f"Division by zero not possible {e}")
    except Exception as e:
        with open(FILE, 'a') as file:
            file.write(f"Error: Unexpected eeror, {e}\n")
        print("Unexpected Error")
    finally:
        print("Thank you for using safe calculator ")
    
