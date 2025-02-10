from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from datetime import datetime

# Get database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

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
    reviews = relationship("Review", back_populates="platform", cascade="all, delete-orphan")

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

def init_db():
    """Initialize database with sample data"""
    # Create all tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Check if data already exists
        if db.query(Platform).first() is None:
            sample_platforms = [
                # Existing platforms
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
                Platform(
                    name="OutSystems",
                    operating_system="Windows",
                    speed_score=95,
                    accuracy_score=92,
                    maintenance_score=85,
                    price_range="$75-499/mo",
                    features="Enterprise Integration, Mobile Development, AI Capabilities"
                ),
                # New platforms
                Platform(
                    name="Mendix",
                    operating_system="Web-based, Windows",
                    speed_score=92,
                    accuracy_score=94,
                    maintenance_score=89,
                    price_range="$50-1000/mo",
                    features="Enterprise Development, Cloud Deployment, AI-Assisted Development"
                ),
                Platform(
                    name="Appian",
                    operating_system="Web-based",
                    speed_score=88,
                    accuracy_score=93,
                    maintenance_score=90,
                    price_range="$90-1500/mo",
                    features="Process Automation, Case Management, RPA Integration"
                ),
                Platform(
                    name="Power Apps",
                    operating_system="Windows, Web-based",
                    speed_score=87,
                    accuracy_score=85,
                    maintenance_score=93,
                    price_range="$10-40/user/mo",
                    features="Microsoft Integration, Mobile Apps, Data Connectors"
                ),
                Platform(
                    name="Salesforce Lightning",
                    operating_system="Web-based",
                    speed_score=86,
                    accuracy_score=89,
                    maintenance_score=94,
                    price_range="$25-400/user/mo",
                    features="CRM Integration, Enterprise Apps, Cloud Development"
                ),
                Platform(
                    name="Zoho Creator",
                    operating_system="Web-based",
                    speed_score=84,
                    accuracy_score=86,
                    maintenance_score=87,
                    price_range="$15-400/mo",
                    features="Business Apps, Workflow Automation, Mobile Development"
                ),
                Platform(
                    name="Retool",
                    operating_system="Web-based",
                    speed_score=91,
                    accuracy_score=88,
                    maintenance_score=86,
                    price_range="$10-50/user/mo",
                    features="Internal Tools, Database Integration, Custom Components"
                ),
                Platform(
                    name="AppSheet",
                    operating_system="Web-based, Mobile",
                    speed_score=83,
                    accuracy_score=85,
                    maintenance_score=88,
                    price_range="$5-10/user/mo",
                    features="Mobile Apps, Data Collection, Offline Functionality"
                ),
                Platform(
                    name="Kissflow",
                    operating_system="Web-based",
                    speed_score=82,
                    accuracy_score=84,
                    maintenance_score=86,
                    price_range="$10-50/user/mo",
                    features="Process Management, Project Management, Case Management"
                ),
                Platform(
                    name="Betty Blocks",
                    operating_system="Web-based",
                    speed_score=88,
                    accuracy_score=87,
                    maintenance_score=85,
                    price_range="$50-800/mo",
                    features="Enterprise Apps, Citizen Development, Block-Based Programming"
                ),
                Platform(
                    name="Quickbase",
                    operating_system="Web-based",
                    speed_score=87,
                    accuracy_score=89,
                    maintenance_score=91,
                    price_range="$500-1000/mo",
                    features="Custom Applications, Workflow Automation, Report Generation"
                ),
                Platform(
                    name="Nintex",
                    operating_system="Web-based, Windows",
                    speed_score=86,
                    accuracy_score=90,
                    maintenance_score=88,
                    price_range="$900-1500/mo",
                    features="Process Automation, Document Generation, Forms Management"
                ),
                Platform(
                    name="WaveMaker",
                    operating_system="Web-based",
                    speed_score=85,
                    accuracy_score=86,
                    maintenance_score=84,
                    price_range="$99-499/mo",
                    features="RAD Platform, Enterprise Apps, Docker Deployment"
                ),
                Platform(
                    name="Caspio",
                    operating_system="Web-based",
                    speed_score=84,
                    accuracy_score=85,
                    maintenance_score=87,
                    price_range="$100-1000/mo",
                    features="Database Apps, Web Forms, Report Builder"
                ),
                Platform(
                    name="Alpha Software",
                    operating_system="Windows, Web-based",
                    speed_score=83,
                    accuracy_score=84,
                    maintenance_score=85,
                    price_range="$99-399/mo",
                    features="Mobile Apps, Offline Capability, Database Integration"
                ),
                Platform(
                    name="Knack",
                    operating_system="Web-based",
                    speed_score=82,
                    accuracy_score=83,
                    maintenance_score=84,
                    price_range="$39-179/mo",
                    features="Database Applications, Online Forms, API Access"
                ),
                Platform(
                    name="TrackVia",
                    operating_system="Web-based",
                    speed_score=81,
                    accuracy_score=84,
                    maintenance_score=83,
                    price_range="$2000-3000/mo",
                    features="Workflow Management, Mobile Apps, Custom Dashboards"
                ),
                Platform(
                    name="Airtable",
                    operating_system="Web-based",
                    speed_score=89,
                    accuracy_score=87,
                    maintenance_score=91,
                    price_range="$10-20/user/mo",
                    features="Database Management, Collaboration, API Integration"
                ),
                Platform(
                    name="FileMaker",
                    operating_system="Windows, MacOS",
                    speed_score=86,
                    accuracy_score=88,
                    maintenance_score=85,
                    price_range="$19-39/user/mo",
                    features="Custom Apps, Database Design, Cross-Platform Development"
                ),
                Platform(
                    name="Glide",
                    operating_system="Web-based",
                    speed_score=88,
                    accuracy_score=85,
                    maintenance_score=89,
                    price_range="$25-99/mo",
                    features="Mobile Apps, No-Code Development, Spreadsheet Integration"
                ),
                Platform(
                    name="Oracle APEX",
                    operating_system="Web-based",
                    speed_score=91,
                    accuracy_score=93,
                    maintenance_score=87,
                    price_range="Free-1000/mo",
                    features="Enterprise Development, Database Apps, REST APIs"
                ),
                Platform(
                    name="Directual",
                    operating_system="Web-based",
                    speed_score=84,
                    accuracy_score=86,
                    maintenance_score=85,
                    price_range="$29-299/mo",
                    features="Backend Development, API Creation, Database Management"
                ),
                Platform(
                    name="Adalo",
                    operating_system="Web-based",
                    speed_score=83,
                    accuracy_score=82,
                    maintenance_score=84,
                    price_range="$50-200/mo",
                    features="Mobile App Development, Visual Design, Component Library"
                ),
                Platform(
                    name="Thunkable",
                    operating_system="Web-based",
                    speed_score=82,
                    accuracy_score=81,
                    maintenance_score=83,
                    price_range="$13-38/mo",
                    features="Mobile Apps, Drag-and-Drop Interface, Cross-Platform"
                ),
                Platform(
                    name="Appgyver",
                    operating_system="Web-based",
                    speed_score=85,
                    accuracy_score=84,
                    maintenance_score=86,
                    price_range="Free-Enterprise",
                    features="Progressive Web Apps, Native Apps, Data Integration"
                ),
                Platform(
                    name="Budibase",
                    operating_system="Web-based",
                    speed_score=87,
                    accuracy_score=86,
                    maintenance_score=88,
                    price_range="Free-100/mo",
                    features="Internal Tools, Automation, Self-Hosting"
                ),
                Platform(
                    name="Stackby",
                    operating_system="Web-based",
                    speed_score=81,
                    accuracy_score=82,
                    maintenance_score=83,
                    price_range="$5-99/user/mo",
                    features="Spreadsheet Database, API Integration, Collaboration"
                ),
                Platform(
                    name="Kintone",
                    operating_system="Web-based",
                    speed_score=84,
                    accuracy_score=85,
                    maintenance_score=86,
                    price_range="$24-200/user/mo",
                    features="Business Apps, Process Management, Team Collaboration"
                ),
                Platform(
                    name="Joget DX",
                    operating_system="Web-based",
                    speed_score=83,
                    accuracy_score=84,
                    maintenance_score=85,
                    price_range="Free-Enterprise",
                    features="Process Automation, Mobile Apps, Open Source"
                )
            ]

            for platform in sample_platforms:
                db.add(platform)

            db.commit()
            print("Sample data initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()