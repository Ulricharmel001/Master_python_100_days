class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def info(self):
        print(f"Author : {self.author}")
        print(f"Title : {self.title}")
# create object 
book1 = Book("Eat That frog", "Brian Tracy")
book1.info()
book2 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
book2.info()

#instance method 
class bankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, New balance: ${self.balance}")

#create object

acc1 = bankAccount("Ulrich Armel",300)
acc1.deposit(800)


# class method 

class myApp:
    app_version = "1.1.0"

    @classmethod
    def get_version(cls):
        print(f"App Version: {cls.app_version}")

    @staticmethod
    def greet():
        print(" Hello my dev!")

myApp.greet()
myApp.get_version()


#  Encapsulation and validation 
# __ on variable name in a class make it a private variable

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.__balance  = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance +=  amount
            print(f"Deposited ${amount}, New Balance:  ${self.__balance}")
        else:
            print("Invalid Deposit Balance")
    def get_balance(self):
        return self.__balance

accc1 = Account("Ulrich Armel", balance=800)
accc1.deposit(900)
print(f"Acount Balance: ${accc1.get_balance()}")



