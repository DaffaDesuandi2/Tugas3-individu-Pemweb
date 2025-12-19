import os
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Review
from schemas import ReviewCreate, ReviewResponse
from ai_sentiment import analyze_sentiment
from ai_keypoints import extract_key_points

# =========================
# LOAD ENV
# =========================
load_dotenv()

# =========================
# FASTAPI APP
# =========================
app = FastAPI(
    title="Product Review Analyzer API",
    description="Backend API untuk menganalisis review produk dengan proses paralel",
    version="1.1.0"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# DATABASE INIT
# =========================
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {"message": "Backend is running smoothly"}

# =========================
# POST REVIEW (OPTIMIZED)
# =========================
@app.post("/api/reviews", response_model=ReviewResponse)
async def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    # 1. Jalankan Analisis AI secara Paralel untuk menghemat waktu
    # Kita menggunakan asyncio.gather agar sentiment dan keypoints diproses bersamaan
    try:
        # Menjalankan fungsi async dari ai_sentiment dan ai_keypoints
        sentiment_task = analyze_sentiment(review.review_text)
        keypoints_task = extract_key_points(review.review_text)
        
        # Tunggu kedua proses selesai (Total waktu = waktu proses terlama)
        (sentiment, confidence), key_points = await asyncio.gather(
            sentiment_task, 
            keypoints_task
        )
    except Exception as e:
        print(f"AI Processing Error: {e}")
        # Default value jika AI gagal agar aplikasi tidak crash
        sentiment, confidence, key_points = "NEUTRAL", 0.0, "Analysis unavailable"

    # 2. Siapkan data untuk Database
    db_review = Review(
        review_text=review.review_text,
        sentiment=sentiment,
        # Pastikan confidence diubah ke string dan dibatasi panjangnya
        confidence=str(round(confidence, 4)) if confidence else "0.0",
        key_points=key_points
    )

    # 3. Simpan ke Database
    try:
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database Error: {str(e)}")

# =========================
# GET REVIEWS
# =========================
@app.get("/api/reviews", response_model=list[ReviewResponse])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).order_by(Review.created_at.desc()).all()