import plotly.express as px

def create_performance_charts(platforms_data):
    """
    Creates performance visualization charts using Plotly Express
    """
    # Prepare data for visualization
    platforms = list(platforms_data.keys())
    speed_ratings = [data["speed_rating"] for data in platforms_data.values()]
    
    fig = px.line(
        x=platforms,
        y=speed_ratings,
        markers=True,
        title="Speed Performance Across Platforms",
        labels={"x": "Platform", "y": "Speed Rating"}
    )
    
    fig.update_traces(line_color='#FF4B4B', marker_color='#FF4B4B')
    fig.update_layout(height=300)
    
    return fig
