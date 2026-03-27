my_tuple = (1,3,4)
fruit = ("orange","Mango","berry")
print(fruit[1])
print(fruit[-1])

# we can change turple but we can change the value of variablea 
number =(1,2,3,4)
w, x, y, z = number
print(w)

# set
my_set = {1,2,3}

my_set.add(4)
print(my_set)
my_set.remove(1)
print(my_set)


set_a = {"flour", "sugar", "rice"}
set_b ={"flour", "sugar"}

#union
print(set_a | set_b)
# difference
print(set_a - set_b)
# intersection
print(set_a & set_b)
print(set_a ^ set_b)