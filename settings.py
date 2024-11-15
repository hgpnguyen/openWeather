import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('OPENWEATHER_API', '')
RETRY_TIMES = 3
MAX_API_RATE = 60