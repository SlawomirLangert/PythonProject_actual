# from logging import exception
# from traceback import print_exc
#
# import requests

# def get_weather():
#     api_key = ""
#     city = ""
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
#
#     try:
#
#
#     except Exception as e:
#         print(e)

import requests
from datetime import datetime
from config import Config
#from common.functions import celvin,speed_wind


def get_weather():
    api_key = Config.api_key
    city = Config.api_city
    excel_path = Config.excel_path
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()

        weather = {
            "temp": data.get("main").get("temp"),
            "feels_like": data.get("main").get("feels_like"),
            "name": data.get("name"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "description": data.get("weather")[0].get("description"),
            "wind_speed": data.get("wind").get("speed")
        }
        return weather
    except Exception as e:
        print(e)


