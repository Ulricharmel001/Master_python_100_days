# read and write in json 


import os, json

TASK_FILE = "data2.json"
#reading  json file
with open(TASK_FILE, 'r') as json_file:
    data = json.load(json_file)
    print(data)


# Writing to a json new file 

tasks = [{"Task": "learning python", "Status": "incomplete"}]

with open("data3.json", 'w') as file :
    json.dump(tasks, file, indent=4)



task_name = input("Enter your task name!")
task_status = input("Enter your task status")
new_task = [{"Task": task_name, "Status": task_status}]

with open('data3.json', 'r') as file:
    task = json.load(file)

    task.append(new_task)


with open('data3.json', 'w') as file:
    json.dump(task, file, indent=4)