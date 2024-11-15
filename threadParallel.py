import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor

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

def get_weather(lat: float, lon: float):
    api_key = os.environ.get('OPENWEATHER_API', '')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
    return response.json()

def parallel(num: int, latMin: float, latMax: float, lonMin: float, lonMax: float):
    positions = get_list_pos(latMin, latMax, lonMin, lonMax)
    tasks = []
    start_time = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        tasks = [executor.submit(get_weather, lat, lon) for _, (lat, lon) in enumerate(positions[:min(num, len(positions))])]
        #results = [task.result() for task in tasks]
    #print(results)
    end_time = time.perf_counter()
    print(f"Elapsed run time of Thread: {end_time - start_time} seconds.")
    return tasks