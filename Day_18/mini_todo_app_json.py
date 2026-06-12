#mini_todo_app_json.py
import json

from prompt_toolkit import choice
TASK_FILE = "tasks.json"
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
   # save tasks 
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
#add task
def add_task():
    task_name = input("Enter task name: ")
    tasks = load_tasks()
    tasks.append({"Task": task_name, "Status": "Incomplete"})
    print(f"Task '{task_name}' added.")
    save_tasks(tasks)
# view tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['Task']} - {task['Status']}")
        #  update status to complete
def mark_task_complete():    
    tasks = load_tasks()
    view_tasks()
    task_num = int(input("Enter task number to update status: "))
    task_status = input("Enter task status: ")
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]['Status'] = task_status
        print(f"Task '{tasks[task_num - 1]['Task']}' marked as {task_status}.")
        save_tasks(tasks)
# delete task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    if 0 < task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task['Task']}' deleted.")
        save_tasks(tasks)
# edit task
def edit_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to edit.")
        return
    view_tasks()
    task_num = int(input("Enter task number to edit: "))
    if 0 < task_num <= len(tasks):
        new_task_name = input("Enter new task name: ")
        tasks[task_num - 1]['Task'] = new_task_name
        print(f"Task '{new_task_name}' updated.")
        save_tasks(tasks)
#
def quit_app():
    print("Exiting the application. Goodbye!")
    exit()
# display menu
def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6  Exit")


# MAIN FUNCTION
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            edit_task()
        elif choice == '6':
            quit_app()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()