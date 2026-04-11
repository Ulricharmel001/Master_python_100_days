# Student grade manager

# step 1 get student scores

studentScores = input(" Enter Students scores seperated by comma: ")
scores = [int(score) for score in studentScores.split(",")]

# assign grade using list comprehension 

grades =[
    "A" if score >= 90 else
    "B" if  score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "D+" if score >= 50 else
    "F"
    for score in scores
]

# filter passsed and failed studens

passedStudents = [score for score in scores if score >=50]
failedStudent  = [score for score in scores if score < 50]

#  display results
print("\n --- Results--- ")
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\n ----Passing And Failling Students----")
print("Passing students:", passedStudents)
print("Failling Students: ", failedStudent)
