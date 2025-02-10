import streamlit as st

def render_metric_card(title, value, delta=None):
    """Render a metric card with optional delta"""
    st.metric(
        label=title,
        value=value,
        delta=delta
    )

def render_platform_details(platform_data, platform_name):
    """Render detailed information for a specific platform"""
    platform_info = platform_data[platform_data['Platform'] == platform_name].iloc[0]
    
    st.subheader(f"{platform_name} Details")
    cols = st.columns(2)
    
    with cols[0]:
        st.write("**Operating Systems:**", platform_info['Operating_Systems'])
        st.write("**Price Range:**", platform_info['Price_Range'])
    
    with cols[1]:
        st.write("**Best For:**", platform_info['Best_For'])
        avg_score = (platform_info['Speed_Score'] + 
                    platform_info['Accuracy_Score'] + 
                    platform_info['Maintenance_Score']) / 3
        st.write("**Average Score:**", f"{avg_score:.1f}")

def render_comparison_table(filtered_data):
    """Render an interactive comparison table"""
    st.dataframe(
        filtered_data.style.background_gradient(
            subset=['Speed_Score', 'Accuracy_Score', 'Maintenance_Score'],
            cmap='YlOrRd'
        ),
        use_container_width=True
    )

def render_filters(os_list):
    """Render filter sidebar"""
    st.sidebar.header("Filters")
    selected_os = st.sidebar.multiselect(
        "Operating System",
        options=os_list,
        default=os_list[0]
    )
    min_speed = st.sidebar.slider(
        "Minimum Speed Score",
        0, 100, 70
    )
    min_accuracy = st.sidebar.slider(
        "Minimum Accuracy Score",
        0, 100, 70
    )
    return selected_os, min_speed, min_accuracy
