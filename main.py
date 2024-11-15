from geopy.geocoders import Nominatim
from dotenv import load_dotenv
from threadParallel import parallel
from asyncParallel import get_cities_weather
from utils import write_to_file
import time

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

def main():
    start_time = time.perf_counter()
    res = get_cities_weather(-5.34, 0.34, 10.99, 15.99)
    end_time = time.perf_counter()
    print(len(res))
    write_to_file("citiesWeather.json", res)
    print(f"Elapsed run time: {end_time - start_time} seconds.")

    #print(len(res))

if __name__=="__main__":
    main()