# Password generator
import random
import  string
FILE_NAME = "password.csv"
def generate_password(length=12):
    if length < 5:
        raise ValueError("Password length must be at least 4 character")
    upperCase = string.ascii_uppercase
    lowerCase = string.ascii_lowercase
    specialCase = string.punctuation
    deigit = string.digits

    password = [
        random.choice(upperCase),
        random.choice(lowerCase),
        random.choice(specialCase),
        random.choice(deigit)
        ]

    # fill the remaining length with random choices from each set 

    allCharacter = upperCase + lowerCase + deigit + specialCase
    password += random.choices(allCharacter, k=length-4)

    # shuffle it to make it more random 

    random.shuffle(password)
    return''.join(password)
  

try:
    length = int(input("Enter the desired length (minimum 5:)"))
    password = generate_password(length)
    print("Generated Password: ", password)
    with open(FILE_NAME, 'a') as file :
        file.write(generate_password(length)+ "\n")
except ValueError as e:
    print(f"Error: {e}")
       
        
        
