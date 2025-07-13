import dotenv
import os

def get_token():
  dotenv.load_dotenv()
  TOKEN = os.getenv('TOKEN')
  return TOKEN
