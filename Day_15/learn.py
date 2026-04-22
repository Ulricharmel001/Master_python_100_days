FILE_NAME = "sample.txt"

with open(FILE_NAME, "r") as file:
    content = file.read()
    print(content)

with open(FILE_NAME, 'r') as file :
    for   line in file:
        print("new line", line.strip())