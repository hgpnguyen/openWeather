from typing import List, Dict, Tuple
import json
import settings

def get_list_pos(lat_min: float, lat_max: float, lon_min: float, lon_max: float):
    lat, lon = lat_min, lon_min
    div = settings.STEP_DIV
    step_lat, step_lon = (lat_max-lat_min)/div, (lon_max-lon_min)/div 
    while lat <= lat_max:
        while lon <= lon_max:
            yield lat, lon
            lon += step_lon
            if step_lon == 0:
                break
        lon = lon_min
        lat += step_lat
        if step_lat == 0:
            break


def filter(weather_data: List[any]) -> Dict[str, any]:
    cities_weather = {}
    for weather in weather_data:
        if weather['name'] and weather['name'] not in cities_weather:
            cities_weather[weather['name']] = weather
    return cities_weather

def write_to_file(file_name: str, cities_weather: Dict[str, any]) -> None:
    with open(file_name, "w") as out_file:
        json.dump(cities_weather, out_file)

def get_min_max(mssg: str, bound_val: float) -> Tuple[float, float]:
    min_str = input(f"Please enter min {mssg} [-{bound_val}, {bound_val}]: ")
    while True:
        try:
            min_bound = float(min_str)
        except:
            min_bound = float('-inf')
        if -bound_val <= min_bound <= bound_val:
            break
        min_str = input(f"Wrong value. Please enter min {mssg} between -{bound_val} and {bound_val}: ")

    max_str = input(f"Please enter max {mssg} [{min_bound}, {bound_val}]: ")
    while True:
        try:
            max_bound = float(max_str)
        except:
            max_bound = float('-inf')
        if min_bound <= max_bound <= bound_val:
            break
        max_str = input(f"Wrong value. Please enter max {mssg} between {min_bound} and {bound_val}: ")
    return min_bound, max_bound

def get_user_input() -> Tuple[float, float, float, float]:
    lat_min, lat_max = get_min_max("latitude", 90)
    lon_min, lon_max = get_min_max("longitude", 180)
    return lat_min, lat_max, lon_min, lon_max
        