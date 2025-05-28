import streamlit as st
import sys
import os

# Add the parent directory to the path so we can import components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import set_page_style, render_header, render_footer, start_content, end_content

# Page config
st.set_page_config(
    page_title="How It Works | Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply the common page style
set_page_style()

# Render the header with How It Works as active
render_header(active_page="How It Works")

# Start the main content area
start_content()

# Title
st.markdown('<div class="title">How It Works</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Understanding the technology behind our Fake News Detection</div>', unsafe_allow_html=True)

# Content
# First, add a container div with proper styling
st.markdown('<div style="max-width: 800px; margin: 0 auto; color: var(--text-secondary);">', unsafe_allow_html=True)

# Add the heading for Machine Learning Approach
st.markdown('<h3 style="color: var(--text-primary); margin-top: 30px;">Our Machine Learning Approach</h3>', unsafe_allow_html=True)

# Add the introduction paragraph
st.markdown('<p>The Fake News Detector uses advanced machine learning algorithms to analyze news content and determine its authenticity. Here\'s how it works:</p>', unsafe_allow_html=True)

# Add the steps as separate elements
# Step 1: Text Preprocessing
st.markdown('''
<div style="background-color: #334155; padding: 20px; border-radius: 10px; margin: 20px 0;">
    <h4 style="color: #3B82F6; margin-top: 0;">1. Text Preprocessing</h4>
    <p>We clean and normalize the input text by removing stop words, punctuation, and applying stemming or lemmatization to reduce words to their base forms.</p>
</div>
''', unsafe_allow_html=True)

# Step 2: Feature Extraction
st.markdown('''
<div style="background-color: #334155; padding: 20px; border-radius: 10px; margin: 20px 0;">
    <h4 style="color: #3B82F6; margin-top: 0;">2. Feature Extraction</h4>
    <p>We convert text into numerical features using techniques like TF-IDF (Term Frequency-Inverse Document Frequency) and word embeddings.</p>
</div>
''', unsafe_allow_html=True)

# Step 3: Model Selection
st.markdown('''
<div style="background-color: #334155; padding: 20px; border-radius: 10px; margin: 20px 0;">
    <h4 style="color: #3B82F6; margin-top: 0;">3. Model Selection</h4>
    <p>We offer multiple machine learning models for analysis:</p>
    <ul>
        <li><strong>SVM (Support Vector Machine)</strong>: Excellent for text classification with high-dimensional data</li>
        <li><strong>XGBoost</strong>: A powerful gradient boosting algorithm that handles complex patterns</li>
        <li><strong>Passive Aggressive</strong>: An online learning algorithm that adapts quickly to new data</li>
    </ul>
</div>
''', unsafe_allow_html=True)

# Step 4: Prediction
st.markdown('''
<div style="background-color: #334155; padding: 20px; border-radius: 10px; margin: 20px 0;">
    <h4 style="color: #3B82F6; margin-top: 0;">4. Prediction</h4>
    <p>The selected model analyzes the features and classifies the news as either "REAL" or "FAKE" based on patterns learned from thousands of pre-labeled examples.</p>
</div>
''', unsafe_allow_html=True)

# Training Data section
st.markdown('<h3 style="color: var(--text-primary); margin-top: 40px;">Training Data</h3>', unsafe_allow_html=True)
st.markdown('''
<p>Our models are trained on a diverse dataset of over 40,000 news articles that have been manually verified for authenticity. This dataset includes:</p>
<ul>
    <li>Mainstream news sources</li>
    <li>Known fake news websites</li>
    <li>Social media content</li>
    <li>Political news from various perspectives</li>
</ul>
''', unsafe_allow_html=True)

# Accuracy and Limitations section
st.markdown('<h3 style="color: var(--text-primary); margin-top: 40px;">Accuracy and Limitations</h3>', unsafe_allow_html=True)
st.markdown('''
<p>While our models achieve over 90% accuracy on test data, it's important to understand their limitations:</p>
<ul>
    <li>Satire can sometimes be misclassified as fake news</li>
    <li>Very recent events may not be accurately classified if they contain new patterns</li>
    <li>Context and nuance can be challenging for machine learning models</li>
</ul>
<p>We recommend using this tool as one of several methods to verify information, alongside checking multiple sources and consulting fact-checking websites.</p>
''', unsafe_allow_html=True)

# Close the container div
st.markdown('</div>', unsafe_allow_html=True)

# End the main content area
end_content()

# Render the footer
render_footer()