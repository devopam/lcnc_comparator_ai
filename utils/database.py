from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from datetime import datetime

# Get database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL')

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base
Base = declarative_base()

class Platform(Base):
    """Platform model for storing platform data"""
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    operating_system = Column(String)
    speed_score = Column(Float)
    accuracy_score = Column(Float)
    maintenance_score = Column(Float)
    price_range = Column(String)
    features = Column(String)
    reviews = relationship("Review", back_populates="platform")

class Review(Base):
    """Review model for storing user reviews and ratings"""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    user_name = Column(String)
    rating = Column(Float)  # 1-5 star rating
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    platform = relationship("Platform", back_populates="reviews")

# Create all tables
Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database with sample data"""
    db = SessionLocal()

    # Check if data already exists
    if db.query(Platform).first() is None:
        sample_platforms = [
            Platform(
                name="Bubble",
                operating_system="Web-based",
                speed_score=85,
                accuracy_score=90,
                maintenance_score=88,
                price_range="$25-299/mo",
                features="Visual Development, API Integration, Database"
            ),
            Platform(
                name="Webflow",
                operating_system="Web-based",
                speed_score=90,
                accuracy_score=88,
                maintenance_score=92,
                price_range="$12-212/mo",
                features="Visual Design, CMS, Hosting"
            ),
            # Add more sample platforms...
        ]

        for platform in sample_platforms:
            db.add(platform)

        db.commit()