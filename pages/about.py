import streamlit as st
import sys
import os

# Add the parent directory to the path so we can import components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components import set_page_style, render_header, render_footer, start_content, end_content

# Page config
st.set_page_config(
    page_title="About | Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply the common page style
set_page_style()

# Render the header with About as active
render_header(active_page="About")

# Start the main content area
start_content()

# Title
st.markdown('<div class="title">About Our Project</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🔍Detect if a news article is Real or Fake using Advanced ML Models</div>', unsafe_allow_html=True)

# Info boxes
st.markdown("""
<div class="stats-dashboard">
    <div class="stat-card">
        <div class="stat-content">
            <div class="stat-header">
                <div class="stat-icon">🤖</div>
                <div class="stat-title">ML Models</div>
            </div>
            <div class="stat-value">3</div>
            <div class="stat-description">SVM, XGBoost, and Passive Aggressive classifiers</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-content">
            <div class="stat-header">
                <div class="stat-icon">✓</div>
                <div class="stat-title">Accuracy</div>
            </div>
            <div class="stat-value">99%</div>
            <div class="stat-description">High precision in detecting fake news articles</div>
        </div>
    </div>
    <div class="stat-card">
        <div class="stat-content">
            <div class="stat-header">
                <div class="stat-icon">⚡</div>
                <div class="stat-title">Fast Detection</div>
            </div>
            <div class="stat-value">&lt;2s</div>
            <div class="stat-description">Real-time analysis and instant results</div>
        </div>
    </div>
</div>

<style>
.stats-dashboard {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 25px;
    margin: 40px auto;
    max-width: 1000px;
}

.stat-card {
    background-color: var(--bg-elevated);
    border-radius: 20px;
    width: 280px;
    overflow: hidden;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    border-top: 4px solid transparent;
    background-image: linear-gradient(to right, var(--bg-elevated), var(--bg-elevated)), 
                      linear-gradient(to right, var(--accent-primary), var(--accent-secondary));
    background-origin: border-box;
    background-clip: padding-box, border-box;
}

.stat-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
}

.stat-content {
    padding: 25px;
}

.stat-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.stat-icon {
    font-size: 24px;
    margin-right: 12px;
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
}

.stat-title {
    font-size: 18px;
    font-weight: 600;
    color: var(--text-primary);
    letter-spacing: 0.5px;
    font-family: 'Manrope', sans-serif;
}

.stat-value {
    font-size: 48px;
    font-weight: 800;
    font-family: 'Space Grotesk', sans-serif;
    margin: 10px 0;
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
}

.stat-description {
    font-size: 15px;
    color: var(--text-secondary);
    margin-bottom: 10px;
    line-height: 1.6;
    font-family: 'IBM Plex Sans', sans-serif;
}

.info-paragraph {
    max-width: 800px;
    margin: 30px auto;
    text-align: center;
    font-size: 18px;
    line-height: 1.7;
    color: var(--text-secondary);
    padding: 0 20px;
}

.info-paragraph strong {
    color: var(--accent-primary);
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Add description paragraph
st.markdown("""
<div class="info-paragraph">
    This powerful tool leverages cutting-edge machine learning models including <strong>Support Vector Machine (SVM)</strong>, <strong>XGBoost</strong>, and <strong>Passive Aggressive Classifier</strong> to verify the authenticity of news content with unprecedented accuracy.
</div>

<style>
.info-paragraph {
    max-width: 800px;
    margin: 30px auto;
    text-align: center;
    font-size: 18px;
    line-height: 1.7;
    color: var(--text-secondary);
    padding: 0 20px;
}

.info-paragraph strong {
    color: var(--accent-primary);
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Features section
st.markdown("""
<style>
.feature-container {
    margin: 60px auto;
    max-width: 1100px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
}

.feature-box {
    position: relative;
    width: 300px;
    background: var(--bg-elevated);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transition: all 0.4s ease;
    display: flex;
    flex-direction: column;
}

.feature-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.feature-icon-area {
    position: relative;
    height: 120px;
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.5s ease;
    overflow: hidden;
}

.feature-box:hover .feature-icon-area {
    transform: scale(1.1);
}

.feature-icon-area::before {
    content: '';
    position: absolute;
    width: 150%;
    height: 100%;
    background: rgba(255, 255, 255, 0.1);
    transform: rotate(45deg) translateX(-100%);
    transition: transform 0.6s ease;
}

.feature-box:hover .feature-icon-area::before {
    transform: rotate(45deg) translateX(100%);
}

.feature-emoji {
    font-size: 48px;
    z-index: 2;
    filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.2));
}

.feature-body {
    padding: 25px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.feature-heading {
    font-size: 22px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 15px;
    font-family: 'Manrope', sans-serif;
    position: relative;
    display: inline-block;
}

.feature-heading::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 40px;
    height: 3px;
    background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
    border-radius: 3px;
}

.feature-text {
    color: var(--text-secondary);
    font-size: 16px;
    line-height: 1.7;
    flex-grow: 1;
    font-family: 'IBM Plex Sans', sans-serif;
}

.feature-cta {
    margin-top: 20px;
    color: var(--accent-primary);
    font-weight: 600;
    display: flex;
    align-items: center;
    font-size: 15px;
    transition: transform 0.3s ease;
}

.feature-cta:hover {
    transform: translateX(5px);
}

.feature-arrow {
    margin-left: 6px;
    transition: transform 0.3s ease;
}

.feature-box:hover .feature-arrow {
    transform: translateX(3px);
}
</style>

<div class="feature-container">
    <div class="feature-box">
        <div class="feature-icon-area">
            <span class="feature-emoji">🎯</span>
        </div>
        <div class="feature-body">
            <div class="feature-heading">High Accuracy</div>
            <div class="feature-text">Our AI models achieve 95%+ accuracy in detecting fake news through advanced machine learning techniques.</div>
        </div>
    </div>
    <div class="feature-box">
        <div class="feature-icon-area">
            <span class="feature-emoji">⚡️</span>
        </div>
        <div class="feature-body">
            <div class="feature-heading">Real-time Analysis</div>
            <div class="feature-text">Analyze news articles in under 2 seconds with our optimized algorithms and parallel processing capabilities, enabling immediate verification during your browsing experience.</div>
        </div>
    </div>
                <div class="feature-box">
        <div class="feature-icon-area">
            <span class="feature-emoji">🧠</span>
        </div>
        <div class="feature-body">
            <div class="feature-heading">Multiple Models</div>
            <div class="feature-text">Leverage the combined intelligence of three state-of-the-art ML models that work together to cross-validate results, ensuring the highest possible detection accuracy.</div>
        </div>
    </div>
</div>

<div style="margin-top: 60px; text-align: center; max-width: 700px; margin-left: auto; margin-right: auto;">
    <h3 style="color: var(--text-primary);">Our Mission</h3>
    <p style="color: var(--text-secondary); line-height: 1.7; font-size: 16px;">
        At UTS, we're committed to combating misinformation through technology. 
        The Fake News Detector project was developed as part of our mission to create tools 
        that help people make more informed decisions about the content they consume online.
    </p>
</div>
""", unsafe_allow_html=True)

# End the main content area
end_content()

# Render the footer
render_footer()