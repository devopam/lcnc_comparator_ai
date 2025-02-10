import streamlit as st
from utils.database import SessionLocal, Review, Platform
from datetime import datetime

def render_review_form(platform_name):
    """Render the review submission form"""
    st.subheader("Submit a Review")
    
    # Create form
    with st.form(key=f"review_form_{platform_name}"):
        user_name = st.text_input("Your Name")
        rating = st.slider("Rating", min_value=1, max_value=5, value=5)
        comment = st.text_area("Your Review")
        submit_button = st.form_submit_button("Submit Review")
        
        if submit_button and user_name and comment:
            db = SessionLocal()
            try:
                # Get platform
                platform = db.query(Platform).filter(Platform.name == platform_name).first()
                if platform:
                    # Create new review
                    new_review = Review(
                        platform_id=platform.id,
                        user_name=user_name,
                        rating=rating,
                        comment=comment,
                        created_at=datetime.utcnow()
                    )
                    db.add(new_review)
                    db.commit()
                    st.success("Thank you for your review!")
            finally:
                db.close()

def display_reviews(platform_name):
    """Display all reviews for a platform"""
    st.subheader("User Reviews")
    
    db = SessionLocal()
    try:
        platform = db.query(Platform).filter(Platform.name == platform_name).first()
        if platform and platform.reviews:
            for review in platform.reviews:
                with st.container():
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.write(f"⭐ {review.rating}/5")
                    with col2:
                        st.write(f"**{review.user_name}**")
                    st.write(review.comment)
                    st.write(f"Posted on: {review.created_at.strftime('%Y-%m-%d %H:%M')}")
                    st.divider()
        else:
            st.info("No reviews yet. Be the first to review!")
    finally:
        db.close()
