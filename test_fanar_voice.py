import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FANAR_API_KEY")

url = "https://api.fanar.qa/v1/audio/speech"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "Fanar-Aura-TTS-2",
    "voice": "default",
    "input": "السلام عليكم، مرحباً بكم في قصة فنار أبطال. هذه قصة تعليمية للأطفال."
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=180
)

print("Status:", response.status_code)

if response.status_code == 200:

    with open("tts_output.mp3", "wb") as f:
        f.write(response.content)

    print("✅ Audio saved successfully as tts_output.mp3")

else:
    print("❌ Error:")
    print(response.text)