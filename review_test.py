from dotenv import load_dotenv
import os
import requests

load_dotenv()

env = os.environ.get("APP_ENV")
print(f"Environment: {env}")

max_retries = os.environ.get("MAX_RETRIES")
print(f"Max Retries: {max_retries}")

urls = [
    "https://github.com",
    "https://google.com",
    "https://fakeexample.com"
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"HTTP OK - {response.status_code}")
        else:
            print(f"HTTP not OK - {response.status_code}")
    except requests.exceptions.ConnectTimeout:
        print("Web server timed out")
    except requests.exceptions.ConnectionError:
        print("Connection error to the web server.")
