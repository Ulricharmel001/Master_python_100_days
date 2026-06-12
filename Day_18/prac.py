import os
import json


TASK_FILE ="Data.json"
with open(TASK_FILE, 'r') as file:
    task = json.load(file)
    print(task)


task = [{"Task": "learning python", "Status": "incomplete"}]

with open("data2.json", 'w') as file :
    json.dump(task, file, indent=4)


with open('data2.json', 'r') as file:
    task = json.load(file)

task.append({"Task":"Learning Nodejs", "Status": "Incomplete"})

with  open("data2.json", 'w') as file:
    json.dump(task, file, indent=4)