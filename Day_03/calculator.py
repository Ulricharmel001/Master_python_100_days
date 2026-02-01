#  vraiable data type 
name  = "ulrich"
age = 34
height = 3.7

print(type(name), type(age), type(height))


# the data type conversion 

height = int(height)
print(height)
age = float(age)
print(age)
print(f" the type of age is {type(age)}")
print(type(height))

# colllect input and convert to another data type
name = input("Enter your name ")
print(f"Hello {name}")

num1 = input("enter the first number--\n")
num1 = int(num1)
print(num1 * 2)

# basic arithmetic operations 
#float division, modulus division(that produce the remainder)

a = 30
b = 15
print(f"Addition : {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Floor Division : {a//b}")
print(f"Modulus : {a%b}")
print(f"Exponential: {a**b}")

# Challenge: Basic calculator 
# simple python program that takes two number from the user and perform basic calculatioons

number1 = int(input(f"Enter the first number.\n"))
number2 = int(input(f"Enter the second number \n"))

# display results

print(f"----Calculation Result----")
print(f"Addition : {number1+number2}")
print(f"Subtraction: {number1-number2}")
print(f"Multiplication: {number1*number2}")
if number2 == 0:
    print("Divion by zero is not allowed ")
    exit()
print(f"Division: {number1/number2}")
print(f"Floor Division : {number1//number2}")
print(f"Modulus : {number1%number2}")
print(f"Exponential: {number1**number2}")
