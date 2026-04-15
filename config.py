import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

class Config:
   api_key = os.getenv("API_KEY")
   api_city = os.getenv("API_CITY")
   #excel_path = os.getenv("EXCEL_PATH")
   filepath = os.getenv("EXCEL_PATH")
   limit_pokemon = os.getenv("LIMIT_POKEMON")