import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
SENTIMENT_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

async def analyze_sentiment(text: str):
    async with httpx.AsyncClient() as client:
        try:
            # Menggunakan wait_for_model=True agar tidak error saat model 'cold start'
            response = await client.post(
                SENTIMENT_URL,
                headers=headers,
                json={"inputs": text, "options": {"wait_for_model": True}},
                timeout=60.0
            )
            data = response.json()
            
            # Ambil skor tertinggi
            best = max(data[0], key=lambda x: x["score"])
            return best["label"], float(best["score"])
        except Exception as e:
            print(f"Sentiment Error: {e}")
            return "UNKNOWN", 0.0