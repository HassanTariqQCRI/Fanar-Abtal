import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FANAR_API_KEY")

response = requests.get(
    "https://api.fanar.qa/v1/models",
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

print("Status:", response.status_code)
print(response.json())