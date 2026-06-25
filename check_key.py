from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("FANAR_API_KEY")

print("KEY FOUND:", key)
print("LENGTH:", len(key) if key else 0)