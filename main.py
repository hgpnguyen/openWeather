from asyncParallel import get_cities_weather
from utils import write_to_file, get_user_input
import time


def main():
    print("Please enter the region.")
    lat_min, lat_max, lon_min, lon_max = get_user_input()
    res = get_cities_weather(lat_min, lat_max, lon_min, lon_max)
    write_to_file("citiesWeather.json", res)
    print("Finish. The weather data are in citiesWeather.json.")


if __name__=="__main__":
    main()