import asyncio
import time
import httpx
import settings
import aiometer
from functools import partial

from utils import get_list_pos, filter

async def get_weather_async(client: httpx.AsyncClient, lat: float, lon: float) -> any:
    api_key = settings.API_KEY
    start = time.perf_counter()
    response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric", timeout=60.0)
    num_retry = 0
    while response.status_code != 200 and num_retry < settings.RETRY_TIMES:
        response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric", timeout=60.0)
        num_retry += 1
    print("Response time: ", time.perf_counter()-start)
    return response.json()

async def async_parallel(lat_min: float, lat_max: float, lon_min: float, lon_max: float):
    positions_gen = get_list_pos(lat_min, lat_max, lon_min, lon_max)
    client = httpx.AsyncClient()
    start = time.perf_counter()
    tasks = [partial(get_weather_async, client, lat, lon) for lat, lon in positions_gen]
    results = await aiometer.run_all(
        tasks,
        max_per_second=settings.MAX_API_RATE,
    )
    print(time.perf_counter()-start)
    return results

def get_cities_weather(lat_min: float, lat_max: float, lon_min: float, lon_max: float):
    weather = asyncio.run(async_parallel(lat_min, lat_max, lon_min, lon_max))
    return filter(weather)