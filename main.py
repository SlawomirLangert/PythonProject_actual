# from math import trunc
#
# from services.excel_files import read_excel
# from services.excel_files import save_to_excel
# from services.openweather_api import get_weather
# from services.pokemon import wszystkie_pokemony
# import pandas as pd
# #from common.functions import celvin
# import time
from config import Config
from services.dashboard import render_dashboard

#file = read_excel(Config.excel_path)
#print(file.describe())

#file = read_excel(Config.excel_path)
dashboard = render_dashboard(Config.filepath)
# while True:
#     lista_pokemonow = wszystkie_pokemony()
#     #print(lista_pokemonow)
#     df = pd.DataFrame(lista_pokemonow)
#     time.sleep(10)

# lista_pokemonow = wszystkie_pokemony()
# #print(lista_pokemonow)
# df = pd.DataFrame(lista_pokemonow)
# print(df)



# while True:
#     weather = get_weather()
#     print(weather)
#     #time.sleep(10)
#     weather = get_weather()
#     save_to_excel([weather])
#     print("Pobrano i zapisano dane")
#     time.sleep(5)

# while True:
#     # weather = get_weather()
#     print(weather)
#     # time.sleep(10)
#     weather = get_weather()
#     save_to_excel([weather])
#     print("Pobrano i zapisano dane")
#     time.sleep(5)