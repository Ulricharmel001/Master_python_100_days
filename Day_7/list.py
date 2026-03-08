shopping_list = ['orange', 'tomato', 'apple']
print(shopping_list)


#accessing list item

print(shopping_list[1])

#list manipulation

shopping_list.append("sugar")
print(shopping_list)

shopping_list.insert(2,"Mango")
print(shopping_list)

# Removing Item from a list 
shopping_list.remove('Mango')
print(shopping_list)
shopping_list.pop()
print(shopping_list)
shopping_list.pop(1)
print(shopping_list)

# looping inside list 

for item in shopping_list:
    print(f"-{item}")

# using  enumerate 

for index, item in enumerate(shopping_list):
    print(f"{index + 1}. {item}")
shopping_list.sort()
print(shopping_list)
shopping_list.reverse()
print(shopping_list)

shopping_list.clear()
print(shopping_list)