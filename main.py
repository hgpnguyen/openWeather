import requests
import os
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
from threadParallel import parallel

load_dotenv()

def get_all_cities(latMin: float, latMax: float, lonMin: float, lonMax: float):
    geolocator = Nominatim(user_agent="abcd")
    cities = set()
    results = []
    lat, lon = latMin, lonMin
    STEP = 0.5
    count = 0
    while lat <= latMax:
        while lon <= lonMax:
            count += 1
            coord = f"{lat},{lon}"
            location = geolocator.reverse(coord, exactly_one=True)
            if not location:
                lon += STEP
                continue
            address = location.raw['address']
            city = address.get('city', '')
            if city and city not in cities:
                cities.add(city)
                results.append((city, lat, lon))
            lon += STEP
        lon = lonMin
        lat += STEP
    print(results)
    print(len(results))
    print(count)
    return results



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
    #weather, status = get_weather(44.34, 10.99)
    #printWeather(weather)
    parallel(200, 44.34, 54.34, 10.99, 20.99)

if __name__=="__main__":
    main()