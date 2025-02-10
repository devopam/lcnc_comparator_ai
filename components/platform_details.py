import streamlit as st
from utils.visualizations import create_radar_chart
from utils.data_handler import get_performance_metrics
from components.reviews import render_review_form, display_reviews

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

    # Add reviews section
    st.markdown("---")
    tab1, tab2 = st.tabs(["Read Reviews", "Write Review"])

    with tab1:
        display_reviews(platform_name)

    with tab2:
        render_review_form(platform_name)