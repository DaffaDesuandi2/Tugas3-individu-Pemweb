import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
SUMMARY_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

async def extract_key_points(text: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SUMMARY_URL,
                headers=headers,
                json={"inputs": text, "options": {"wait_for_model": True}},
                timeout=60.0
            )
            data = response.json()
            return data[0]["summary_text"]
        except Exception as e:
            print(f"Keypoints Error: {e}")
            return "Could not extract key points."