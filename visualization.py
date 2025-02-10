import plotly.express as px
import plotly.graph_objects as go

def create_radar_chart(platform_data, selected_platforms):
    """Create radar chart for platform comparison"""
    metrics = ['Speed_Score', 'Accuracy_Score', 'Maintenance_Score']
    filtered_data = platform_data[platform_data['Platform'].isin(selected_platforms)]
    
    fig = go.Figure()
    for platform in selected_platforms:
        platform_scores = filtered_data[filtered_data['Platform'] == platform][metrics].values[0]
        fig.add_trace(go.Scatterpolar(
            r=platform_scores,
            theta=metrics,
            name=platform,
            fill='toself'
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="Platform Comparison Radar Chart"
    )
    return fig

def create_bar_chart(platform_data, metric):
    """Create bar chart for single metric comparison"""
    fig = px.bar(
        platform_data,
        x='Platform',
        y=metric,
        title=f'{metric.replace("_", " ")} Comparison',
        color=metric,
        color_continuous_scale='Viridis'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def create_scatter_plot(platform_data):
    """Create scatter plot comparing speed vs accuracy"""
    fig = px.scatter(
        platform_data,
        x='Speed_Score',
        y='Accuracy_Score',
        text='Platform',
        size='Maintenance_Score',
        title='Speed vs Accuracy (Size represents Maintenance Score)',
        color='Maintenance_Score',
        color_continuous_scale='Viridis'
    )
    return fig
