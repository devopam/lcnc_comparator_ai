import streamlit as st
import pandas as pd

def render_comparison_matrix(df):
    """Render the comparison matrix component"""
    st.subheader("Platform Comparison Matrix")
    
    # Create a styled dataframe
    styled_df = df.style.background_gradient(
        cmap='YlOrRd',
        subset=[col for col in df.columns if col.endswith('_Score')]
    )
    
    # Display the styled dataframe
    st.dataframe(styled_df, height=400)
    
    # Add download button
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Comparison Data",
        data=csv,
        file_name="platform_comparison.csv",
        mime="text/csv"
    )

def render_feature_checklist(feature_matrix):
    """Render the feature comparison checklist"""
    st.subheader("Feature Comparison")
    st.dataframe(feature_matrix, height=300)
