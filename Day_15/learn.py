FILE_NAME = "sample.txt"

with open(FILE_NAME, "r") as file:
    content = file.read()
    print(content)

with open(FILE_NAME, 'r') as file :
    for   line in file:
        print("new line", line.strip())


try:
    with open('index', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(" Error : File not found")