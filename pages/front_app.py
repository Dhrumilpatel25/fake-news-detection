import streamlit as st
import time
import random
import sys
import os

# Add the parent directory to the path so we can import components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import set_page_style, render_header, render_footer, start_content, end_content, styled_button

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply the common page style
set_page_style()

# Render the header with Detector as active
render_header(active_page="Detector")

# Start the main content area
content_container = start_content()

# Use the container for all content
with content_container:
    # Title and Subtitle
    st.markdown('<div class="title">Fake News Detector</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Fact-check news headlines with ML-powered models</div>', unsafe_allow_html=True)
    
    # Create a container with some padding for the form
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        # Text input
        news_text = st.text_area("Paste the news headline below", height=150)
        
        # Model choice
        model_choices = ['Passive Aggressive', 'SVM', 'XGBoost']
        model_choice = st.selectbox("🤖 Select Model", model_choices)
        
        # Check button
        if styled_button("Check if it's Fake or Real", button_type="success", key="check_btn", use_container_width=True, icon="🔍", size="small"):
            if not news_text.strip():
                st.error("Please enter some text.")
            else:
                # Demo mode - simulate a prediction
                with st.spinner("Analyzing text..."):
                    # Simulate processing time
                    time.sleep(2)
                    # For demo purposes, randomly choose between REAL and FAKE
                    # In a real app, you would use your ML model here
                    label = random.choice(["REAL", "FAKE"])
                    
                    if label == "REAL":
                        st.markdown('<div class="result-box real-result">This headline appears to be REAL.</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="result-box fake-result">This headline appears to be FAKE.</div>', unsafe_allow_html=True)
                    
                    st.info(f"Model used: {model_choice} (Demo mode)")

# End the main content area
end_content()

# Render the footer
render_footer()