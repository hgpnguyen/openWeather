import requests
import os
import geo
from dotenv import load_dotenv
load_dotenv()

def get_weather(lon: float, lat: float):
    api_key = os.environ.get('OPENWEATHER_API', '')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
    return response.json(), response.status_code

def printWeather(weatherJson):
    weatherMssg = f"City: {weatherJson['name']}, Longitude: {weatherJson['coord']['lon']}, Latitude: {weatherJson['coord']['lat']}\n"
    weatherDescription = ', '.join([weather['description'] for weather in weatherJson['weather']])
    weatherMssg += f"Weather: {weatherDescription}, Temperature: {weatherJson['main']['temp']} Celsius, Humidity: {weatherJson['main']['humidity']}%, Pressure: {weatherJson['main']['pressure']} hPa"
    print(weatherMssg) 

def main():
    weather, status = get_weather(44.34, 10.99)
    printWeather(weather)

if __name__=="__main__":
    main()