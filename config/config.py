import dotenv
import os

def get_token():
  dotenv.load_dotenv(dotenv_path='.env')
  TOKEN = os.getenv('TOKEN')
  return TOKEN
