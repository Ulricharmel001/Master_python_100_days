# Working with weather data from an API
In this project, we will be working with the OpenWeatherMap API to get weather data for a specific location. 
We will be using the `requests` library to make HTTP requests to the API and the `json` library to parse the response.

## tasks complete the following tasks to build a simple weather application:
1. Sign up for a free API key at https://openweathermap.org/api.
2. Create a Python script that takes a city name as input and retrieves the current weather data for that city using the OpenWeatherMap API.
3. Parse the JSON response to extract and display the following information:
   - City name
   - Current temperature (in Celsius)
   - Weather description (e.g., clear sky, rain, etc.)
   - Humidity percentage
   - Wind speed (in meters per second)	
4. Handle any potential errors that may occur during the API request (e.g., invalid city name, network issues, etc.) and display an appropriate error message to the user.

## Challenge task 
- allow the user to input multiple city names separated by commas and display the weather data for each city in a formatted manner.
- allow the user to view focast data for the next 5 days for a specific city, including the expected temperature and weather conditions for each day.
- implement a feature that allows the user to save the retrieved weather data to a local file (e.g., CSV or JSON) for future reference.
- display sunrise and sunset times for the specified city, converting the timestamps from the API response into a human-readable format.
