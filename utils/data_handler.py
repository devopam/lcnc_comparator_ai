import pandas as pd
from .database import SessionLocal, Platform
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_platform_data():
    """Returns platform data as a pandas DataFrame"""
    db = SessionLocal()
    try:
        logger.info("Fetching platform data from database")
        platforms = db.query(Platform).all()
        logger.info(f"Found {len(platforms)} platforms")

        if not platforms:
            logger.warning("No platforms found in database")
            return pd.DataFrame()

        data = {
            'Platform': [p.name for p in platforms],
            'Operating_System': [p.operating_system for p in platforms],
            'Speed_Score': [p.speed_score for p in platforms],
            'Accuracy_Score': [p.accuracy_score for p in platforms],
            'Maintenance_Score': [p.maintenance_score for p in platforms],
            'Price_Range': [p.price_range for p in platforms],
            'Features': [p.features for p in platforms]
        }

        df = pd.DataFrame(data)
        logger.info(f"Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
        return df
    except Exception as e:
        logger.error(f"Error fetching platform data: {str(e)}")
        raise
    finally:
        db.close()

def filter_by_os(df, os_filter):
    """Filter platforms by operating system"""
    if os_filter == "All":
        return df
    return df[df['Operating_System'].str.contains(os_filter)]

def get_performance_metrics(platform_name):
    """Get detailed performance metrics for a specific platform"""
    db = SessionLocal()
    try:
        platform = db.query(Platform).filter(Platform.name == platform_name).first()
        return {
            'speed': platform.speed_score,
            'accuracy': platform.accuracy_score,
            'maintenance': platform.maintenance_score
        }
    finally:
        db.close()

def get_feature_comparison():
    """Generate feature comparison matrix"""
    df = get_platform_data()
    features = set()
    for feature_list in df['Features']:
        features.update([f.strip() for f in feature_list.split(',')])

    comparison_matrix = {}
    for platform in df['Platform']:
        platform_features = df[df['Platform'] == platform]['Features'].iloc[0]
        comparison_matrix[platform] = {
            feature: '✓' if feature in platform_features else '✗'
            for feature in features
        }

    return pd.DataFrame(comparison_matrix).T