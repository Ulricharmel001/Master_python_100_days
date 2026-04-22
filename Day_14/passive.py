import random, string

# print(math.sqrt(23))


# def add(a,b):
#     return a + b


# password = "".join(r.choices("iidqjeif90482347t57hfebvsdfbvjk;AKJCBHFVBHFEV", k=2))
# print(password)


# Random password generator

FILE_NAME = "password.csv"

def generatePassword(min_length = 5):
    if min_length < 5:
        raise ValueError("Your password must be at least 5 character :")
    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    specialCase = string.punctuation
    digit = string.digits

    password =[
        random.choice(lowerCase),
        random.choice(upperCase),
        random.choice(digit),
        random.choice(specialCase)
    ]

    all_chars = lowerCase + upperCase + digit + specialCase
    password += random.choices(all_chars, k=min_length-5 )

    random.shuffle(password)

    return "".join(password)

try:
    min_length = int(input("Enter your desired password length(minimum 5):"))
    print("Generated Password : ", generatePassword(min_length))  
    with open(FILE_NAME, 'a') as file:
        file.write(generatePassword(min_length) + "\n")
except ValueError as e:
    print(f"Error:{e}")





