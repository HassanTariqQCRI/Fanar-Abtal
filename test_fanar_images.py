import os
import json
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FANAR_API_KEY")

url = "https://api.fanar.qa/v1/images/generations"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "Fanar-Oryx-IG-2",
    "prompt": "Islamic children's storybook cover showing a smiling Muslim girl with her parents, kindness, colorful illustration, Ramadan lanterns, Qatar, cartoon storybook style"
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=180
)

print("Status:", response.status_code)
print(response.text)

if response.status_code == 200:
    data = response.json()

    try:
        image_data = data["data"][0]["b64_json"]

        image_bytes = base64.b64decode(image_data)

        with open("generated_cover.png", "wb") as image_file:
            image_file.write(image_bytes)

        print("Image saved successfully as generated_cover.png")

    except Exception as e:
        print("Could not save image.")
        print(e)
else:
    print("Image generation failed.")