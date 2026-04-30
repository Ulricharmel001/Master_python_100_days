# Recipe Viewer App
# step 1 : load recipe
def load_recipe(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            recipes = content.split('\n\n')
            recipe_dic = {}
            for recipe in recipes:
                lines = recipe.strip().split('\n')
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('Ingredients:', '').strip()
                    instructions = lines[2].replace('Instructions:', '').strip()
                  
                    recipe_dic[name] = {"ingredients": ingredients, "instructions": instructions}
            return recipe_dic
    except FileNotFoundError:
        print("Error: File not found!!")
        return {} # Return empty dict to prevent errors later

# step 2 Display Recipe Menu
def show_menu():
    print("\n--- Recipe Viewer Menu---")
    print("1. View All Recipes")
    print("2. View Recipe by Name")
    print("3. Exit App")
  

# step 3 display recipe details
def view_recipe(recipes):
    name = input("Enter the name of the recipe : ").strip()
    if name in recipes:
        print(f"\n---- Recipe {name} Details---")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']} ")
    else:
        print("Recipe not found")
# Step 4 : add new recipe
def add_recipe(recipes):
    try:
        with open('recipe.txt', 'a') as file:
            name = input("Enter the name of the new recipe: ").strip()
            ingredients = input("Enter the ingredients (comma separated): ").strip()
            instructions = input("Enter the instructions: ").strip()
            
            if name in recipes:
                print("Recipe already exists!")
            else:
                file.write(f"{name}\nIngredients: {ingredients}\nInstructions: {instructions}\n\n")
                recipes[name] = {"ingredients": ingredients, "instructions": instructions}
                print(f"Recipe '{name}' added successfully!")
    except Exception as e:        
        print(f"Error adding recipe: {e}")

# step 5 : Main program
recipe_file = 'recipe.txt'
recipes = load_recipe(recipe_file)

if recipes is not None:
    while True:
        show_menu()
        choice = input("Enter your choice [1/2/3/4]: ")
        if choice == '1':
            print("\n--All Recipes--")
            for name in recipes:
                print(f"- {name}")
        elif choice == '2':
            view_recipe(recipes)
        elif choice == '3':
            add_recipe(recipes)
        elif choice == '4':
            print("Exiting program!")
            break
