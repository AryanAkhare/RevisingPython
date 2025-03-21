from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_curr_weather(city="Nagpur"): #default city Nagpur
    request_url=f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data=requests.get(request_url).json()

    return weather_data
if __name__=="__main__":
    print(f'\n*** Get Current Weather Conditions ***\n')

    city=input("\nPlease enter a city name : ")
    # Checking empty string
    if not bool(city.strip()):
        city="Nagpur"

    weather_data=get_curr_weather(city)
    print("\n")
    pprint(weather_data)