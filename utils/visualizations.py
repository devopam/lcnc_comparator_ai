import plotly.express as px
import plotly.graph_objects as go
from utils.database import SessionLocal, Review, Platform
from datetime import datetime, timedelta
import pandas as pd

def create_radar_chart(platform_metrics, platform_name):
    """Create radar chart for platform metrics"""
    categories = ['Speed', 'Accuracy', 'Maintenance']
    values = [
        platform_metrics['speed'],
        platform_metrics['accuracy'],
        platform_metrics['maintenance']
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=platform_name
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title=f"{platform_name} Performance Metrics"
    )
    return fig

def create_comparison_bar_chart(df, metric):
    """Create bar chart for comparing platforms on a specific metric"""
    fig = px.bar(
        df,
        x='Platform',
        y=f'{metric}_Score',
        title=f'{metric} Comparison Across Platforms',
        color='Platform',
        labels={f'{metric}_Score': f'{metric} Score'}
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        height=400
    )
    return fig

def create_scatter_plot(df):
    """Create scatter plot for speed vs accuracy"""
    fig = px.scatter(
        df,
        x='Speed_Score',
        y='Accuracy_Score',
        text='Platform',
        title='Speed vs Accuracy Comparison',
        labels={
            'Speed_Score': 'Speed Score',
            'Accuracy_Score': 'Accuracy Score'
        }
    )
    fig.update_traces(textposition='top center')
    return fig

def create_review_heatmap(platform_name=None):
    """Create a heatmap visualization of user reviews"""
    db = SessionLocal()
    try:
        # Calculate date range (last 30 days)
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=30)

        # Query reviews
        query = db.query(Review, Platform)
        if platform_name:
            query = query.join(Platform).filter(Platform.name == platform_name)
        else:
            query = query.join(Platform)

        reviews = query.filter(Review.created_at >= start_date).all()

        # Prepare data for heatmap
        data = []
        for review, platform in reviews:
            data.append({
                'Platform': platform.name,
                'Rating': review.rating,
                'Day': review.created_at.strftime('%Y-%m-%d')
            })

        if not data:
            return None

        df = pd.DataFrame(data)

        # Pivot data for heatmap
        heatmap_data = df.pivot_table(
            values='Rating',
            index='Platform',
            columns='Day',
            aggfunc='mean'
        ).fillna(0)

        # Create heatmap
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='RdYlGn',
            hoverongaps=False
        ))

        fig.update_layout(
            title='Review Ratings Heat Map (Last 30 Days)',
            xaxis_title='Date',
            yaxis_title='Platform',
            height=400
        )

        return fig
    finally:
        db.close()