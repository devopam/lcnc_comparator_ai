import pandas as pd

# Sample data for low-code/no-code platforms
platforms_data = {
    'Platform': [
        'Bubble', 'Webflow', 'Adalo', 'OutSystems', 
        'Mendix', 'Power Apps', 'AppSheet', 'Retool'
    ],
    'Operating_Systems': [
        'Web-based', 'Web-based', 'iOS/Android/Web', 'Windows/Linux/Mac',
        'Windows/Linux', 'Windows/Web', 'All platforms', 'Web-based'
    ],
    'Speed_Score': [85, 90, 75, 95, 88, 82, 78, 92],
    'Accuracy_Score': [90, 88, 82, 94, 92, 85, 80, 89],
    'Maintenance_Score': [85, 92, 78, 90, 88, 86, 82, 88],
    'Price_Range': [
        '$25-$115/mo', '$15-$45/mo', '$50-$200/mo', 'Custom',
        'Custom', '$10-$40/user', '$5-$10/user', '$10-$50/user'
    ],
    'Best_For': [
        'Web Apps', 'Websites', 'Mobile Apps', 'Enterprise',
        'Enterprise', 'Business Apps', 'Mobile/Web Apps', 'Internal Tools'
    ]
}

def get_platform_data():
    return pd.DataFrame(platforms_data)

def get_metrics():
    return ['Speed_Score', 'Accuracy_Score', 'Maintenance_Score']

def get_os_list():
    df = get_platform_data()
    os_list = []
    for os_string in df['Operating_Systems']:
        os_list.extend([os.strip() for os in os_string.split('/')])
    return list(set(os_list))
