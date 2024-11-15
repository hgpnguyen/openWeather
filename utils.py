from typing import List, Dict, Tuple
import json

def get_list_pos(latMin: float, latMax: float, lonMin: float, lonMax: float):
    positions = []
    lat, lon = latMin, lonMin
    DIV = 10
    stepLat, stepLon = (latMax-latMin)/DIV, (lonMax-lonMin)/DIV 
    while lat <= latMax:
        while lon <= lonMax:
            positions.append((lat, lon))
            lon += stepLon
        lon = lonMin
        lat += stepLat
    return positions

def filter(weatherData: List[any]) -> Dict[str, any]:
    citiesWeather = {}
    for weather in weatherData:
        if weather['name'] not in citiesWeather:
            citiesWeather[weather['name']] = weather
    return citiesWeather

def write_to_file(fileName: str, citiesWeather: Dict[str, any]) -> None:
    with open(fileName, "w") as outFile:
        json.dump(citiesWeather, outFile)

def get_user_input() -> Tuple[float, float, float, float]:
    latMin = input("Please enter")