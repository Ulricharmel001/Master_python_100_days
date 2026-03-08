# My shopping list App 


Shopping_list = []

# saving the shopping list to a file and  loading the shopping list from a file, if the file exist, load the shopping list from the file, if not create a new file and save the shopping list to the file when the user exit the app
import os
file_name = "shopping_list.txt"
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        Shopping_list = file.read().splitlines()
else:
    with open(file_name, "w") as file:
        file.write("")
        

def save_shopping_list():
    with open(file_name, "w") as file:
        for item in Shopping_list:
            file.write(item + "\n")

def load_shopping_list():
    with open(file_name, "r") as file:
        return file.read().splitlines()
    


        

def menu():
    print("\n1- show list")
    print("2- Add Item")
    print("3- delete Item")
    print("4- Clear List")
    print("5- Edit Item")
    print("6- Exit App\n")



while True:
    print("\n---Welcome to Shopping list App---")
    menu()
    choice = input(" Enter the opeartion you wish to carry out (1-6)\n")

    if choice == "1":
        print("---Shopping List---\n")
        if not Shopping_list:
            print("Shopping List is Empty")
        for index, item in enumerate(Shopping_list):
            print(f"{index + 1}. {item}")

    elif choice == "2":
         new_item = input("Enter your item \n")
         Shopping_list.append(new_item)
         save_shopping_list()
         print(f"{new_item}, Added successfully")
    elif choice == "3":
        Item_to_delete = input("Enter the item you wish to delete\n")
        try:
            Shopping_list.remove(Item_to_delete)
            save_shopping_list()
            print(f"{Item_to_delete}, has been deleted!")
        except ValueError:
            print(f"{Item_to_delete} not found in shopping list")

    elif choice == "4":
        opinion = input("Are you sure you wish to delete all item? (yes/no)\n").lower()
        if opinion == "yes":
            Shopping_list.clear()
            print(" All item deleted successfully")
        else:
            continue

# edit item using the index of the item in the list, if the item exist in the list, update it with the new item, if not print item not found in shopping list
    elif choice == "5":
        item_to_edit = input("Enter the number of the item you wish to edit\n")
        try:
            index = int(item_to_edit) - 1
            if 0 <= index < len(Shopping_list):
                new_item = input("Enter the new item\n")
                old_item = Shopping_list[index]
                Shopping_list[index] = new_item
                save_shopping_list()
                print(f"{old_item}, has been updated to {new_item} successfully")
        except (ValueError, IndexError):
            print(f"{item_to_edit}, not found in shopping list")

        
    

    elif choice == "6":
        exit_opinion = input("Are you sure you want to quit app? (yes/no)\n").lower()
        if exit_opinion == "yes":
            print("Goodbye, Happy shopping! ")
            break
        else:
            continue
    else:
        print("incorrect Value")
            

          
