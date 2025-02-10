import streamlit as st
import plotly.express as px
from components.comparison_matrix import create_comparison_matrix
from components.performance_charts import create_performance_charts
from components.platform_details import show_platform_details
from data_handler import load_platform_data
from utils.data_transformations import filter_platforms

def main():
    st.set_page_config(
        page_title="Low-Code/No-Code Platform Comparison",
        page_icon="🔄",
        layout="wide"
    )

    st.title("Low-Code/No-Code Platform Comparison Tool")
    
    # Load data
    platforms_data = load_platform_data()
    
    # Sidebar filters
    st.sidebar.title("Filters")
    
    selected_os = st.sidebar.multiselect(
        "Operating System",
        options=["Windows", "macOS", "Linux", "Web-based"],
        default=["Windows", "macOS", "Linux", "Web-based"]
    )
    
    min_speed = st.sidebar.slider(
        "Minimum Speed Rating",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.5
    )
    
    # Filter data based on selections
    filtered_data = filter_platforms(platforms_data, selected_os, min_speed)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Platform Comparison Matrix")
        comparison_table = create_comparison_matrix(filtered_data)
        st.plotly_chart(comparison_table, use_container_width=True)
    
    with col2:
        st.subheader("Speed Metrics")
        speed_chart = create_performance_charts(filtered_data)
        st.plotly_chart(speed_chart, use_container_width=True)
    
    # Platform details section
    st.subheader("Platform Details")
    show_platform_details(filtered_data)
    
    # Methodology explanation
    with st.expander("Methodology"):
        st.write("""
        Our comparison metrics are based on:
        - Speed: Average time to complete common development tasks
        - Accuracy: Success rate in achieving desired outcomes
        - Maintenance: Ease of updating and maintaining applications
        - OS Compatibility: Supported operating systems and environments
        
        Ratings are calculated using aggregated user feedback and performance benchmarks.
        """)

if __name__ == "__main__":
    main()
