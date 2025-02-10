def filter_platforms(platforms_data, selected_os, min_speed):
    """
    Filters platform data based on selected criteria
    """
    filtered_data = {}
    
    for platform, data in platforms_data.items():
        # Check if any of the platform's OS is in selected_os
        os_match = any(os in selected_os for os in data["os_compatibility"])
        speed_match = data["speed_rating"] >= min_speed
        
        if os_match and speed_match:
            filtered_data[platform] = data
    
    return filtered_data
