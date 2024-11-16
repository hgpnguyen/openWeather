import asyncio
import httpx
import settings
import aiometer

from functools import partial
from utils import get_list_pos, filter

# Get weather data for a position (latitude, longitude)
async def get_weather_async(client: httpx.AsyncClient, lat: float, lon: float) -> any:
    api_key = settings.API_KEY
    response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric", timeout=60.0)
    num_retry = 0
    # Retry if fail
    while response.status_code != 200 and num_retry < settings.RETRY_TIMES:
        response = await client.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric", timeout=60.0)
        num_retry += 1
    return response.json()

# Parallel execution for API call using async
async def async_parallel(lat_min: float, lat_max: float, lon_min: float, lon_max: float):
    positions_gen = get_list_pos(lat_min, lat_max, lon_min, lon_max)
    client = httpx.AsyncClient()
    tasks = [partial(get_weather_async, client, lat, lon) for lat, lon in positions_gen]
    results = await aiometer.run_all(
        tasks,
        max_per_second=settings.MAX_API_RATE, # Maximum number of API requests per second
    )
    return results

# Get all weather data in a region
def get_cities_weather(lat_min: float, lat_max: float, lon_min: float, lon_max: float):
    weather = asyncio.run(async_parallel(lat_min, lat_max, lon_min, lon_max))
    return filter(weather)