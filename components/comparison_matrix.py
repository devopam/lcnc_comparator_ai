import streamlit as st
import pandas as pd

def render_comparison_matrix(df):
    """Render the comparison matrix component"""
    st.subheader("Platform Comparison Matrix")

    if df.empty:
        st.error("No platform data available. Please check the database connection.")
        return

    # Format numeric columns to show as percentages
    numeric_cols = [col for col in df.columns if col.endswith('_Score')]
    df_display = df.copy()
    for col in numeric_cols:
        df_display[col] = df_display[col].apply(lambda x: f"{x:.1f}%")

    # Configure column widths with improved visibility
    column_config = {
        'Platform': st.column_config.TextColumn(
            width='medium',
            help="Platform name"
        ),
        'Operating_System': st.column_config.TextColumn(
            width='medium',
            help="Compatible operating systems"
        ),
        'Price_Range': st.column_config.TextColumn(
            width='small',
            help="Price range for the platform"
        ),
        'Features': st.column_config.TextColumn(
            width='large',
            help="Available features"
        )
    }

    # Add score columns to configuration
    for col in numeric_cols:
        column_config[col] = st.column_config.TextColumn(
            width='small',
            help=f"{col.replace('_Score', '')} performance score"
        )

    # Display total number of platforms
    st.caption(f"Total Platforms: {len(df_display)}")

    # Display the dataframe with improved formatting and increased height
    st.dataframe(
        df_display,
        height=1200,  # Further increased height
        use_container_width=True,
        hide_index=True,
        column_config=column_config
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

    # Configure column widths for feature matrix
    feature_column_config = {
        col: st.column_config.TextColumn(width='small')
        for col in feature_matrix.columns
    }

    # Display total features and platforms
    st.caption(f"Comparing {len(feature_matrix.columns)} features across {len(feature_matrix)} platforms")

    st.dataframe(
        feature_matrix,
        height=800,  # Increased height
        use_container_width=True,
        column_config=feature_column_config
    )

    # Add feature matrix download button
    csv = feature_matrix.to_csv()
    st.download_button(
        label="Download Feature Matrix",
        data=csv,
        file_name="feature_matrix.csv",
        mime="text/csv",
        key="feature_matrix_download"
    )