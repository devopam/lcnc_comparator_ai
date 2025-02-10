import streamlit as st
import pandas as pd
from utils.database import SessionLocal, Platform

def calculate_monthly_cost(base_price, users, storage_gb, features_count):
    """Calculate monthly cost based on parameters"""
    # Basic calculation formula
    user_cost = users * 10  # $10 per user
    storage_cost = storage_gb * 0.5  # $0.5 per GB
    feature_cost = features_count * 5  # $5 per additional feature
    
    return base_price + user_cost + storage_cost + feature_cost

def get_platform_base_prices():
    """Get base prices for all platforms"""
    db = SessionLocal()
    try:
        platforms = db.query(Platform).all()
        prices = {}
        for platform in platforms:
            # Extract numeric value from price range (e.g., "$25-299/mo" -> 25)
            base_price = int(platform.price_range.split('-')[0].replace('$', ''))
            prices[platform.name] = base_price
        return prices
    finally:
        db.close()

def render_cost_calculator():
    """Render the cost analysis calculator"""
    st.header("Cost Analysis Calculator")
    
    # Get base prices for all platforms
    platform_prices = get_platform_base_prices()
    
    # User inputs
    col1, col2 = st.columns(2)
    
    with col1:
        users = st.number_input("Number of Users", min_value=1, value=5)
        storage = st.number_input("Storage Needed (GB)", min_value=1, value=10)
    
    with col2:
        features = st.number_input("Additional Features Needed", min_value=0, value=2)
        timeframe = st.selectbox("Billing Period", ["Monthly", "Annually"])
    
    # Calculate costs for each platform
    costs = {}
    for platform, base_price in platform_prices.items():
        monthly_cost = calculate_monthly_cost(base_price, users, storage, features)
        annual_cost = monthly_cost * 12
        costs[platform] = {
            "Monthly": monthly_cost,
            "Annually": annual_cost,
            "Annual Savings": monthly_cost * 12 * 0.1  # 10% discount for annual billing
        }
    
    # Display results
    st.subheader("Cost Comparison")
    
    # Create comparison table
    comparison_data = []
    for platform, cost_data in costs.items():
        comparison_data.append({
            "Platform": platform,
            f"Cost ({timeframe})": cost_data[timeframe],
            "Monthly Cost": cost_data["Monthly"],
            "Annual Cost": cost_data["Annually"],
            "Potential Annual Savings": cost_data["Annual Savings"]
        })
    
    df = pd.DataFrame(comparison_data)
    
    # Format currency columns
    currency_cols = [col for col in df.columns if "Cost" in col or "Savings" in col]
    for col in currency_cols:
        df[col] = df[col].apply(lambda x: f"${x:,.2f}")
    
    st.dataframe(df, use_container_width=True)
    
    # Add cost breakdown explanation
    with st.expander("See Cost Breakdown"):
        st.markdown("""
        ### Cost Components
        - **Base Price**: Platform's starting price
        - **User Cost**: $10 per user per month
        - **Storage Cost**: $0.5 per GB per month
        - **Feature Cost**: $5 per additional feature per month
        
        ### Annual Discount
        - 10% discount applied for annual billing
        """)
