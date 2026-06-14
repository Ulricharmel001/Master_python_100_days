import dotenv
import os
import requests

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")

city = input("Which city do you want the weather for? ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)
weather_data = response.json()
if response.status_code == 200:
    print(f"The weather in {city} is {weather_data}.")
else:
    print(f"Sorry, I couldn't get the weather for {city}.")