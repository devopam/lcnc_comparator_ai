import streamlit as st
import pandas as pd
from utils.data_handler import get_platform_data, get_performance_metrics
from utils.visualizations import create_radar_chart

def render_comparison_slider():
    """Render the interactive platform comparison slider"""
    st.subheader("Interactive Platform Comparison")
    
    # Get platform data
    df = get_platform_data()
    platforms = df['Platform'].tolist()
    
    # Create two columns for platform selection
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Platform A")
        platform_a = st.selectbox(
            "Select first platform",
            platforms,
            key="platform_a"
        )
        
        # Get and display metrics for platform A
        metrics_a = get_performance_metrics(platform_a)
        st.metric("Speed Score", f"{metrics_a['speed']}%")
        st.metric("Accuracy Score", f"{metrics_a['accuracy']}%")
        st.metric("Maintenance Score", f"{metrics_a['maintenance']}%")
        
        # Display radar chart for platform A
        radar_a = create_radar_chart(metrics_a, platform_a)
        st.plotly_chart(radar_a, use_container_width=True)
        
        # Display features for platform A
        features_a = df[df['Platform'] == platform_a]['Features'].iloc[0]
        st.markdown("#### Features")
        for feature in features_a.split(','):
            st.markdown(f"- {feature.strip()}")
    
    with col2:
        st.markdown("### Platform B")
        platform_b = st.selectbox(
            "Select second platform",
            [p for p in platforms if p != platform_a],
            key="platform_b"
        )
        
        # Get and display metrics for platform B
        metrics_b = get_performance_metrics(platform_b)
        st.metric("Speed Score", f"{metrics_b['speed']}%")
        st.metric("Accuracy Score", f"{metrics_b['accuracy']}%")
        st.metric("Maintenance Score", f"{metrics_b['maintenance']}%")
        
        # Display radar chart for platform B
        radar_b = create_radar_chart(metrics_b, platform_b)
        st.plotly_chart(radar_b, use_container_width=True)
        
        # Display features for platform B
        features_b = df[df['Platform'] == platform_b]['Features'].iloc[0]
        st.markdown("#### Features")
        for feature in features_b.split(','):
            st.markdown(f"- {feature.strip()}")
    
    # Display price comparison
    st.markdown("### Price Comparison")
    price_comparison = pd.DataFrame({
        'Platform': [platform_a, platform_b],
        'Price Range': df[df['Platform'].isin([platform_a, platform_b])]['Price_Range'].tolist()
    })
    st.dataframe(price_comparison, use_container_width=True)
