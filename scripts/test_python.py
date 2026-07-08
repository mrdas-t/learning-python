import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("API_KEY")
db_password = os.environ.get("DB_PASSWORD")
