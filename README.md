<!-- GETTING STARTED -->
## About The Project
This is a simple CLI Python application that retrieves weather data from the OpenWeather API for a specific region. This application optimizes the time it takes to collect weather data from multiple locations within the region by using parallel API calls.
## Getting Started

This is an example of how you can set up this project locally.
Please follow these simple example steps to set up this project locally.

### Prerequisites

Install Python
* Python
    ```sh
    sudo apt-get update
    sudo apt-get install python3.8
Obtain OpenWeather API key
* Login or sign up an account on https://home.openweathermap.org
* In the top right corner, click on your username and choose "My API keys"
* Get your default key there or generate a new one

### Installation
1. Setup virtual environment
    ```sh
    pip install virtualenv
    python3 -m venv <virtual-environment-name>
    source <virtual-environment-name>/bin/activate
    ```
2. Install requirement packages
    ```sh
    python3 install -r requirement.txt
    ```
3. Create .env that contains OpenWeather API key. Example of .env file:
    ```sh
    OPENWEATHER_API=<YOUR_API_KEY>
    ```
4. Run `main.py` and enter a bounding box that covers the area from (`lat_min`, `lon_min`) to (`lat_max`, `lon_max`)
    ```sh
    python3 main.py
    ```

5. The retrieve weather data for multiple cities are stored in citiesWeather.json
## Usage
Example: Retrieve weather data for multiple cities within a area from (-5.5, 10) to (5, 15)
```sh
> python3 main.py
Please enter the region.
Please enter min latitude [-90, 90]: -5
Please enter max latitude [-5.0, 90]: 5
Please enter min longitude [-180, 180]: 10
Please enter max longitude [10.0, 180]: 15
Finish. The weather data are in citiesWeather.json.
```
## Explanation & Justification
- For parallel execution, at first I used `threading` because retrieving OpenWeather API is an io-bound operation so using `threading` is faster than `multiprocessing`. After that, after running some test I found out that `asyncio` library is faster than `threading` library so I choose to use `asyncio` and `httpx` library for parallel API calls.
- To implement a way to limit the amount of OpenWeather API calls per second, I use `aiometer` library which allows user to limit the number of tasks spawned per second.
- To collect the weather data for multiple cities within a region, I split the region equally into maximum of 121 positions to collect data and filter out any duplicate.
## Room for improvement
- Improve fault tolerant: when request fails, should have specific way to deal with specific status code.
- Should find a way to collect all cities in region before collect their weather data. The current method may miss some city especially when the region becomes bigger.
