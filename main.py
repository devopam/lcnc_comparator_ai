import streamlit as st
import pandas as pd
from utils.data_handler import get_platform_data, filter_by_os, get_feature_comparison
from utils.visualizations import create_comparison_bar_chart, create_scatter_plot
from components.comparison_matrix import render_comparison_matrix, render_feature_checklist
from components.platform_details import render_platform_details
from components.cost_calculator import render_cost_calculator
from components.comparison_slider import render_comparison_slider

# Page configuration
st.set_page_config(
    page_title="Low-Code/No-Code Platform Comparison",
    page_icon="🔄",
    layout="wide"
)

# Main title
st.title("Low-Code/No-Code Platform Comparison Tool")
st.markdown("""
Compare different low-code and no-code platforms across various metrics including
speed, accuracy, and maintenance aspects.
""")

# Get data
df = get_platform_data()

# Sidebar filters
st.sidebar.header("Filters")
os_filter = st.sidebar.selectbox(
    "Operating System",
    ["All", "Windows", "Linux", "Web-based", "Mobile"]
)

# Filter data
filtered_df = filter_by_os(df, os_filter)

# Main content
tab1, tab2, tab3, tab4 = st.tabs([
    "Comparison Matrix",
    "Performance Analysis",
    "Feature Comparison",
    "Cost Calculator"
])

with tab1:
    # Add the comparison slider at the top
    render_comparison_slider()
    st.markdown("---")
    # Original comparison matrix below
    render_comparison_matrix(filtered_df)

with tab2:
    # Performance metrics visualization
    col1, col2 = st.columns(2)

    with col1:
        speed_chart = create_comparison_bar_chart(filtered_df, "Speed")
        st.plotly_chart(speed_chart, use_container_width=True, key="speed_comparison_chart")

    with col2:
        scatter_plot = create_scatter_plot(filtered_df)
        st.plotly_chart(scatter_plot, use_container_width=True, key="speed_accuracy_scatter")

    # Platform details
    selected_platform = st.selectbox(
        "Select Platform for Detailed Analysis",
        filtered_df['Platform'].tolist()
    )
    render_platform_details(selected_platform)

with tab3:
    feature_matrix = get_feature_comparison()
    render_feature_checklist(feature_matrix)

with tab4:
    render_cost_calculator()

# Methodology explanation
with st.expander("Methodology"):
    st.markdown("""
    ### How we calculate scores

    - **Speed Score**: Evaluated based on application build time, runtime performance, and deployment speed
    - **Accuracy Score**: Measured through user testing, error rates, and output consistency
    - **Maintenance Score**: Based on update frequency, documentation quality, and community support

    Data is collected through:
    1. User surveys
    2. Performance testing
    3. Expert reviews
    4. Community feedback
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Created with ❤️ using Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)