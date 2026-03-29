FILE = 'note.txt'

with open(FILE, 'w') as file:
    file.write("\n This is the only note")

with open(FILE, 'r') as file:
    content = file.read()
    print(content)

with open(FILE, 'a') as file:
    file.write("\n This is newly added text")