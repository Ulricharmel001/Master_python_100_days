my_dict = {
    "my name": "John",  
    "my age": 30,
    "my city": "New York"

}

print(my_dict["my name"])  # Output: John
print(my_dict["my age"])   # Output: 30
print(my_dict["my city"])  # Output: New York

# .get() method
print(my_dict.get("my name"))  # Output: John
print(my_dict.get("my age"))   # Output: 30
print(my_dict.get("my city"))  # Output: New York


#modify the value of a key
my_dict["my age"] = 31
print(my_dict["my age"])   # Output: 31
# add a new key-value pair
my_dict["my profession"] = "Software Engineer"
print(my_dict["my profession"])  # Output: Software Engineer

# print complete dictionary
print(my_dict)  # Output: {'my name': 'John', 'my age':}

# changing value of a key
my_dict['my age']=50
print(my_dict)

#Add and removing items
my_dict['salary']=1500

print(my_dict)

# deleting entry 

del my_dict["my age"]
print(my_dict)


# looping
for key, value in my_dict.items():
    print(f'{key}: {value}')