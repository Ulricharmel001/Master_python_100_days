class Car:
    def __init__(self, make, model, year, brand):
        self.make = make
        self.model = model
        self.year = year
        self.brand = brand

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        print(f"Car Brand: {self.brand}")

# create an object of the Car class
car1 = Car("Toyota", "Camry", 2020, "Toyota")
# display the car information
car1.display_info()
print(car1.make)
print(car1.model)

class person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old.")

    #create an object of the person class
person1 = person("John", "Doe", 30)
person1.greet()
print(person1.first_name)
print(person1.last_name)
print(person1.age)
        