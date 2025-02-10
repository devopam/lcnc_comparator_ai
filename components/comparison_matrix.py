import streamlit as st
import pandas as pd

def render_comparison_matrix(df):
    """Render the comparison matrix component"""
    st.subheader("Platform Comparison Matrix")

    # Format numeric columns to show as percentages
    numeric_cols = [col for col in df.columns if col.endswith('_Score')]
    df_display = df.copy()
    for col in numeric_cols:
        df_display[col] = df_display[col].apply(lambda x: f"{x:.1f}%")

    # Adjust column widths and formatting
    st.dataframe(
        df_display,
        height=600,  # Increased height
        use_container_width=True,
        hide_index=True  # Hide index for cleaner look
    )

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
    st.dataframe(
        feature_matrix,
        height=500,  # Increased height
        use_container_width=True
    )

    # Add feature matrix download button
    csv = feature_matrix.to_csv()
    st.download_button(
        label="Download Feature Matrix",
        data=csv,
        file_name="feature_matrix.csv",
        mime="text/csv",
        key="feature_matrix_download"  # Added unique key
    )