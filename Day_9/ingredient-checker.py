# ingredient Checker 

# step1 : define the recipe ingredients
recipe_ingredient = {"flour","water","eggs","butter","oil"}

# step 2 Get user ingredient
user_input = input("Enter your available ingredient (seperated by comma): ").lower()
user_ingredient = set(user_input.split(", "))

# step 3 compare user input with the recipe
missing_ingredient = recipe_ingredient - user_ingredient
extra_ingredient = user_ingredient - recipe_ingredient

# step 4 display result 
print("\n----Ingredient Checker Result----")

if missing_ingredient:
    print(f"The following ingredient are missing: {", ".join(missing_ingredient)}")
else:
    print("You have all needed ingredient.")

if extra_ingredient:
    print(f"You have extra ingredient: {", ".join(extra_ingredient)}")
else:
    print("You have all ingredient needed! ")