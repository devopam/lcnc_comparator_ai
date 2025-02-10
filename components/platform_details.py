import streamlit as st
from utils.visualizations import create_radar_chart
from utils.data_handler import get_performance_metrics

def render_platform_details(platform_name):
    """Render detailed platform information"""
    st.header(f"{platform_name} Details")
    
    metrics = get_performance_metrics(platform_name)
    
    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Speed Score", f"{metrics['speed']}%")
    with col2:
        st.metric("Accuracy Score", f"{metrics['accuracy']}%")
    with col3:
        st.metric("Maintenance Score", f"{metrics['maintenance']}%")
    
    # Display radar chart
    radar_chart = create_radar_chart(metrics, platform_name)
    st.plotly_chart(radar_chart)
