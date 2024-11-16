<!-- GETTING STARTED -->
## About The Project
This CLI Python application retrieves weather data from the OpenWeather API for a specified region, optimizing data collection from multiple locations using parallel API calls.
## Setup Guide

Follow these steps to set up the project locally.

### Prerequisites

**Install Python**

```sh
sudo apt-get update
sudo apt-get install python3.8
```
**Obtain OpenWeather API Key:**
* Sign in or create an account at [OpenWeather](https://home.openweathermap.org)
* Click your username at the top right and select "My API keys".
* Retrieve your default key or generate a new one.

### Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/hgpnguyen/openWeather.git
   ```
2. **Set up a virtual environment:**
    ```sh
    pip install virtualenv
    python3 -m venv <virtual-environment-name>
    source <virtual-environment-name>/bin/activate
    ```
3. **Install required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4. **Create a `.env` file with your OpenWeather API key:**
    ```sh
    OPENWEATHER_API=<YOUR_API_KEY>
    ```
5. **Run `main.py` and input the region coordinates (latitude/longitude):**
    ```sh
    python3 main.py
    ```

6. **Weather data for multiple cities will be saved in `citiesWeather.json`.**
## Usage
Example: Retrieve weather data for a region between coordinates (-5.5, 10) and (5, 15):
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
- **Parallel Execution**: Initially used `threading` for its efficiency with I/O-bound operations instead of `multiprocessing`, but tests showed `asyncio` combined with `httpx` was faster, so `asyncio` was chosen for parallel API calls.
- **Rate Limiting**: Implemented using the `aiometer` library to control the number of API calls per second.
- **Weather Data Collection**: The region is divided into a maximum of 121 positions for data collection, filtering out duplicates.
## Room for improvement
- **Enhance Fault Tolerance**: Implement specific handling for different HTTP status codes when requests fail.
- **Weather Data Collection**: Find a more effective method to identify all cities within a region to ensure no city is missed, especially for larger areas.
