
import os, json

TASK_FILE = "data3.json"
#reading  json file
with open(TASK_FILE, 'r') as json_file:
    task = json.load(json_file)
    print(task)



