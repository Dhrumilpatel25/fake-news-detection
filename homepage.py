import streamlit as st
import os
from components import set_page_style, render_header, render_footer, start_content, end_content, styled_button

# --- Page Config ---
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply the common page style
set_page_style()

# Render the header with Home as active
render_header(active_page="Home")

# Start the main content area
content_container = start_content()

# Use the container for all content
with content_container:
    # --- Title and Subtitle ---
    st.markdown('<div class="title">Welcome to Fake News Detector!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Detect if a news article is Real or Fake using ML models</div>', unsafe_allow_html=True)
    
    # --- Logo with animation ---
    st.markdown("""
    <div style='text-align: center; margin: 30px 0; animation: bounce 1.5s ease-out;'>
        <img src='https://img.icons8.com/fluency/96/000000/news.png' width='120' style='display: block; margin-left: auto; margin-right: auto;' />
    </div>
    
    <style>
    @keyframes bounce {
      0%, 100% {
        transform: translateY(0);
      }
      50% {
        transform: translateY(-15px);
      }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # --- Description ---
    st.markdown("""
    <div style="max-width: 700px; margin: 0 auto 15px; text-align: center; color: var(--text-secondary); font-size: 18px; line-height: 1.7;">
    This powerful tool leverages machine learning models such as <strong>SVM</strong>, <strong>XGBoost</strong>,
    <strong>Logistic Regression</strong>, and <strong>PassiveAggressive</strong> to verify the authenticity of news content.
    Click "Get Started" to enter a headline or article and get a real-time prediction!
    </div>
    """, unsafe_allow_html=True)
    
    # --- Get Started Button ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if styled_button("Get Started", button_type="primary", key="get_started_btn", use_container_width=True, icon="🚀", size="large"):
            st.switch_page("./pages/front_app.py")

# End the main content area
end_content()

# Render the footer
render_footer()