import pandas as pd

def filter_platforms(df, selected_os, min_speed, min_accuracy):
    """Filter platforms based on selected criteria"""
    if selected_os:
        mask = df['Operating_Systems'].apply(
            lambda x: any(os in x for os in selected_os)
        )
        df = df[mask]
    
    df = df[
        (df['Speed_Score'] >= min_speed) &
        (df['Accuracy_Score'] >= min_accuracy)
    ]
    
    return df

def get_top_platforms(df, metric, n=3):
    """Get top N platforms based on specific metric"""
    return df.nlargest(n, metric)[['Platform', metric]]
