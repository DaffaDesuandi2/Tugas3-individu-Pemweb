from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# GANTI sesuai database kamu
DATABASE_URL = "postgresql://postgres:S3patusuper!@localhost:5432/product_review_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
