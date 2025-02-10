import pandas as pd
import numpy as np

# Sample data for low-code/no-code platforms
PLATFORM_DATA = {
    'Platform': [
        'Bubble', 'Webflow', 'Adalo', 'OutSystems',
        'Mendix', 'Power Apps', 'AppSheet', 'Retool'
    ],
    'Operating_System': [
        'Web-based', 'Web-based', 'Web/Mobile',
        'Windows/Linux', 'Windows/Linux', 'Windows',
        'Web-based', 'Web-based'
    ],
    'Speed_Score': [85, 90, 75, 95, 92, 88, 82, 87],
    'Accuracy_Score': [90, 88, 82, 94, 93, 89, 85, 86],
    'Maintenance_Score': [88, 92, 80, 90, 89, 85, 83, 84],
    'Price_Range': [
        '$25-299/mo', '$12-212/mo', '$50-200/mo',
        'Custom', 'Custom', '$10-40/user',
        '$12-15/user', '$10-50/user'
    ],
    'Features': [
        'Visual Development, API Integration, Database',
        'Visual Design, CMS, Hosting',
        'Mobile Apps, API Integration',
        'Enterprise, AI, Multi-platform',
        'Enterprise, IoT, Multi-platform',
        'Microsoft Integration, Business Apps',
        'Google Integration, Mobile Apps',
        'Internal Tools, Database Integration'
    ]
}

def get_platform_data():
    """Returns platform data as a pandas DataFrame"""
    return pd.DataFrame(PLATFORM_DATA)

def filter_by_os(df, os_filter):
    """Filter platforms by operating system"""
    if os_filter == "All":
        return df
    return df[df['Operating_System'].str.contains(os_filter)]

def get_performance_metrics(platform_name):
    """Get detailed performance metrics for a specific platform"""
    df = get_platform_data()
    platform = df[df['Platform'] == platform_name].iloc[0]
    return {
        'speed': platform['Speed_Score'],
        'accuracy': platform['Accuracy_Score'],
        'maintenance': platform['Maintenance_Score']
    }

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
