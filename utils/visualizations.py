import plotly.express as px
import plotly.graph_objects as go

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
