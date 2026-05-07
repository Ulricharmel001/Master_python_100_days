#Reading csv
import csv 
with open('text.csv', 'r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#reading dict
with open('text.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


with open('new_student.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Math', 'French', 'English'])
    writer.writerow(['Ulrich', 12, 13, 14])

with open("new_student.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Math', 'French', 'English'])
    writer.writeheader()
    writer.writerow({'Name': 'Evans', 'Math': 25, 'French': 13, 'English':15})

    