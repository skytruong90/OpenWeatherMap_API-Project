import requests
import json

api_key = "YOUR_API_KEY"  # replace with your own API key from OpenWeatherMap

# get location input from user
location = input("Enter the city name: ")

# construct API URL
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(location, api_key)

# send API request and get response
response = requests.get(url)

# parse JSON data from response
data = json.loads(response.text)

# check for valid response
if data["cod"] != 200:
    print("Error: ", data["message"])
else:
    # extract relevant weather data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    # print weather report
    print("Temperature: {:.1f}°C".format(temperature))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed: {} m/s".format(wind_speed))
    print("Description: {}".format(description))
