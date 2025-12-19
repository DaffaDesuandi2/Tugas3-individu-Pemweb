from pydantic import BaseModel

class ReviewCreate(BaseModel):
    review_text: str

class ReviewResponse(BaseModel):
    id: int
    review_text: str
    sentiment: str | None = None
    confidence: str | None = None
    key_points: str | None = None

    class Config:
        from_attributes = True
