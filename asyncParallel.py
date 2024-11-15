import asyncio
import os
import time
import httpx

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

async def get_weather_async(client, lat: float, lon: float):
    api_key = os.environ.get('OPENWEATHER_API', '')
    response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric", timeout=60.0)
    if response.status_code != 200:
        print(response)
    return response.json()

async def async_parallel(num: int, latMin: float, latMax: float, lonMin: float, lonMax: float):
    positions = get_list_pos(latMin, latMax, lonMin, lonMax)
    numRequest = len(positions)
    tasks, results = [], []
    start_time = time.perf_counter()
    for start in range(0, num, num):
        async with httpx.AsyncClient() as client:
            tasks.extend(await asyncio.gather(
                *[get_weather_async(client, lat, lon) for lat, lon in positions[start:min(start+num, numRequest)]]
            ))

    end_time = time.perf_counter()
    print(f"Elapsed run time of Async: {end_time - start_time} seconds.")
    return tasks