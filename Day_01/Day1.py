# Day 1 of 100 days of python challenge
# welcome message generator 

# step 1 ask user details 
name = input("What is your name?").upper()
city = input("Which city do you live in?").upper()
hobby = input("what is your favorite hobby?").upper()
age = int(input("How old are you?").upper())

# generate a personalise welcome message
print("\n---Welcome Message---")
print(f"Hello {name}")
print(f"your city is {city}")
print(f"you love {hobby}")
print(f"and you are {age} years old!")
print("---------------------")
print("Welcome to 100 days of python challenge!")
print("---------------------")
print("Let's code and have fun!")


