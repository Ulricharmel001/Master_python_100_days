# define convesion functions

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit + 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32 ) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


def show_menu():
    print("--- Temperature converter Menu---")
    print("1. Celsius to Celsius & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Fahrenheit and Celsius")
    print("4. Exit")


# main program loop

while True:
    try:
        show_menu()
        choice =input("Enter your choice [1/2/3/4]\n")


        if choice == "1":
            celsius = float(input("Enter temperature in Celsius\n"))
            print(f"Fahrenheit : {celsius_to_fahrenheit(celsius):.2f}")
            print(f"Kelvin: {celsius_to_kelvin(celsius):.2f}")
        elif choice == "2":
            fahrenheit = float(input("Enter your temperature in Fahrenheit\n"))
            print(f"Kelvin : {fahrenheit_to_kelvin(fahrenheit):.2f}")
            print(f"Celsius : {fahrenheit_to_celsius(fahrenheit):.2f}")
        elif choice == "3":
            kelvin = float(input("Enter temperature in Kelvin!\n"))
            print(f"Celsius: {kelvin_to_celsius(kelvin):.2f}")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")
        elif choice == "4":
            confirm = input("Are you sure you want to exit app [yes/no]?")
            if confirm.lower() == "yes":
                break
            else:
                print("Exit cancelled")
                continue

        else:
            print("Invalid input! choose from [1/2/3/4]")
    except ValueError:
        print("invalid input, enter the correct input [1/2/3/4]")
    except TypeError:
        print("Error: input only number from 1-4")
    finally:
        print("Thank you for using Temperature Converter!")
