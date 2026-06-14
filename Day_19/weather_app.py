# Weather app using OpenWeatherMap API
import json
import dotenv
import os
import requests

# set up API key from environment variable
dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# get weather data for a specific city
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            weather_data = {
                "city": weather_data["name"],
                "temperature in Celsius": weather_data["main"]["temp"] - 273.15, # convert from Kelvin to Celsius
                "description": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"],
                "wind_speed": weather_data["wind"]["speed"],   
                "sunrise": weather_data["sys"]["sunrise"],
                "sunset": weather_data["sys"]["sunset"]
            }

            return weather_data
        elif response.status_code == 404:
            print(f"City '{city}' not found. Please check the city name and try again.")
            return None
        else:
            print(f"Error fetching weather data for {city}. Status code: {response.status_code}")
            return None
       
    except requests.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None 
def export_weather_data(weather_data, filename="weather_data.json"):
    import json
    choice = input("Do you want to specify a filename for the exported weather data? (yes/no): ").strip().lower()
    if choice == "yes":
        filename = input("Enter the filename (with .json extension): ").strip()
        if not filename.endswith(".json"):
            print("Invalid filename. Defaulting to 'weather_data.json'.")
            filename = "weather_data.json"
    
    else:
        print("Invalid choice. Defaulting to 'weather_data.json'.")

    try:
        with open(filename, "w") as file:
            json.dump(weather_data, file, indent=4)
        print(f"Weather data exported to {filename}")
    except IOError as e:
        print(f"Error exporting weather data: {e}")


def forecast_for_5_days(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        forecast_data = response.json()
        choice = input("Do you want to export the 5-day forecast data to a file? (yes/no): ").strip().lower()
        if choice == "yes":
            filename = input("Enter the filename for the forecast data (with .json extension): ").strip()
            if not filename.endswith(".json"):
                print("Invalid filename. Defaulting to 'forecast_data.json'.")
                filename = "forecast_data.json"
            try:
                with open(filename, "w") as file:
                    json.dump(forecast_data, file, indent=4)
                print(f"5-day forecast data exported to {filename}")
            except IOError as e:
                print(f"Error exporting forecast data: {e}")
        return forecast_data

    else:
        print(f"Sorry, I couldn't get the forecast for {city}. Status code: {response.status_code}")
        return None

def multiple_cities_weather(cities):
    weather_data_list = []
    for city in cities:
        weather_data = get_weather(city)
        if weather_data:
            weather_data_list.append(weather_data)
            choice = input(f"Do you want to export the weather data for {city} to a file? (yes/no): ").strip().lower()
            if choice == "yes":
                filename = input(f"Enter the filename for {city} weather data (with .json extension): ").strip()
                if not filename.endswith(".json"):
                    print("Invalid filename. Defaulting to 'weather_data.json'.")
                    filename = "weather_data.json"
                try:
                    with open(filename, "w") as file:
                        json.dump(weather_data, file, indent=4)
                    print(f"Weather data for {city} exported to {filename}")
                except IOError as e:
                    print(f"Error exporting weather data for {city}: {e}")
    return weather_data_list


  # display weather data in a user-friendly format  
def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature in Celsius']:.2f}°C")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"Sunrise: {weather_data['sunrise']}")
        print(f"Sunset: {weather_data['sunset']}")
    else:
        print("No weather data to display.")

def menu():
    print("Welcome to the Weather App!")
    print("1. Get weather for a single city")
    print("2. Get weather for multiple cities")
    print("3. Export weather data to a file")
    print("4. Get 5-day forecast for a city")
    print("5. Exit")
# main loop to get user input and display weather data
while True:
    menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        city = input("Enter the city name: ")
        weather_data = get_weather(city)
        display_weather(weather_data)
    elif choice == "2":
        cities = input("Enter city names separated by commas: ").split(",")
        cities = [city.strip() for city in cities]
        weather_data_list = multiple_cities_weather(cities)
        for weather_data in weather_data_list:
            display_weather(weather_data)
    elif choice == "3":
        city = input("Enter the city name to export weather data: ")
        weather_data = get_weather(city)
        if weather_data:
            export_weather_data(weather_data)
    elif choice == "4":
        city = input("Enter the city name for 5-day forecast: ")
        forecast_data = forecast_for_5_days(city)
        if forecast_data:
            print(f"5-day forecast for {city}:")
            for forecast in forecast_data["list"]:
                print(f"Date & Time: {forecast['dt_txt']}, Temperature: {forecast['main']['temp'] - 273.15:.2f}°C, Description: {forecast['weather'][0]['description']}")
    elif choice == "5":
        print("Exiting the Weather App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")