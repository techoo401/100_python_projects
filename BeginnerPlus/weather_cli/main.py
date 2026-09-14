import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code != 200:
    print("City not found!")
    exit()

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
condition = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]

print("Temperature:", temperature, "°C")
print("Feels Like:", feels_like, "°C")
print("Humidity:", humidity, "%")
print("Condition:", condition)
print("Wind Speed:", wind_speed, "m/s")