import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('OPENWEATHER_API', '') # Open Weather API
RETRY_TIMES = 3 # Number retry if fail
MAX_API_RATE = 60 # Maximum number of API per second
STEP_DIV = 10 # Divide for bounding box