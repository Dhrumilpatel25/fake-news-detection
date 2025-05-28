import streamlit as st

def set_page_style():
    """Set the common page style for all pages"""
    st.markdown("""
    <style>
    /* Global Styles and Dark Mode */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;500;600;700&display=swap');
    
    :root {
        --bg-primary: #0F172A;
        --bg-secondary: #1E293B;
        --bg-elevated: #334155;
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --accent-primary: #3B82F6;
        --accent-secondary: #3B82F6;
        --border-color: #334155;
        --success-color: #10B981;
        --error-color: #ef4444;
        --warning-color: #F59E0B;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--text-primary);
        background-color: var(--bg-primary);
    }
    
    /* Page structure */
    .app-container {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    
    .content-wrapper {
        flex: 1;
        width: 100%;
        max-width: 1280px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Hide sidebar collapse control */
    [data-testid="collapsedControl"] {
        display: none;
    }
    
    /* Header Styles */
    .header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        background-color: var(--bg-secondary);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 24px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        z-index: 1000;
    }
    
    .header-left {
        display: flex;
        align-items: center;
    }
    
    .logo-text {
        font-size: 22px;
        font-weight: 700;
        font-family: 'Space Grotesk', sans-serif;
        margin-left: 12px;
        color: var(--accent-primary);
        letter-spacing: 0.5px;
    }
    
    .header-right {
        display: flex;
        gap: 8px;
    }
    
    .nav-item {
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 500;
        font-size: 15px;
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        text-decoration: none;
        transition: all 0.2s ease;
        letter-spacing: 0.2px;
    }
    
    .nav-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
    }
    
    .nav-item.active {
        background-color: var(--accent-primary);
        color: white;
    }
    
    /* Main Content Area */
    .main-content-wrapper > div {
        padding: 30px;
        background-color: var(--bg-secondary);
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        margin: 30px auto 100px auto;
        max-width: 1200px;
        min-height: calc(100vh - 250px);
    }
    
    /* Footer Styles */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: var(--bg-secondary);
        color: var(--text-secondary);
        text-align: center;
        padding: 20px 0;
        font-size: 14px;
        font-family: 'IBM Plex Sans', sans-serif;
        border-top: 1px solid var(--border-color);
        z-index: 999;
    }
    
    /* Form Elements */
    .stTextArea textarea {
        background-color: var(--bg-elevated);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        color: var(--text-primary);
        font-size: 16px;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .stTextArea > label {
        color: var(--text-primary);
        font-weight: 500;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .stSelectbox > label {
        color: var(--text-primary);
        font-weight: 500;
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: var(--bg-elevated);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        color: var(--text-primary);
        font-family: 'IBM Plex Sans', sans-serif;
    }
    
    /* Button Styles */
    .stButton > button {
        background-color: var(--accent-primary);
        color: white;
        font-weight: 600;
        font-family: 'Manrope', sans-serif;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(59, 130, 246, 0.4);
    }
    
    /* Custom Button Classes */
    .primary-button button {
        background-color: var(--accent-primary);
        color: white;
        box-shadow: 0 4px 6px rgba(59, 130, 246, 0.25);
    }
    
    .primary-button button:hover {
        background-color: var(--accent-primary);
        filter: brightness(110%);
        box-shadow: 0 6px 15px rgba(59, 130, 246, 0.4);
    }
    
    .secondary-button button {
        background-color: transparent;
        color: var(--accent-primary);
        border: 1px solid var(--accent-primary);
    }
    
    .secondary-button button:hover {
        background-color: rgba(59, 130, 246, 0.1);
    }
    
    .success-button button {
        background-color: var(--success-color);
        color: white;
        box-shadow: 0 4px 6px rgba(34, 197, 94, 0.25);
    }
    
    .success-button button:hover {
        background-color: var(--success-color);
        filter: brightness(110%);
        box-shadow: 0 6px 15px rgba(34, 197, 94, 0.4);
    }
    
    /* Special styling for the Check if it's Fake or Real button */
    .stButton button u {
        text-decoration: underline !important;
    }
    
    .warning-button button {
        background-color: var(--warning-color);
        color: white;
        box-shadow: 0 4px 6px rgba(245, 158, 11, 0.25);
    }
    
    .warning-button button:hover {
        background-color: var(--warning-color);
        filter: brightness(110%);
        box-shadow: 0 6px 15px rgba(245, 158, 11, 0.4);
    }
    
    .danger-button button {
        background-color: var(--error-color);
        color: white;
        box-shadow: 0 4px 6px rgba(239, 68, 68, 0.25);
    }
    
    .danger-button button:hover {
        background-color: var(--error-color);
        filter: brightness(110%);
        box-shadow: 0 6px 15px rgba(239, 68, 68, 0.4);
    }
    
    .ghost-button button {
        background-color: transparent;
        color: var(--text-secondary);
        border: none;
        box-shadow: none;
    }
    
    .ghost-button button:hover {
        background-color: rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
        transform: none;
        box-shadow: none;
    }
    
    /* Button Sizes */
    .small-button button {
        font-size: 14px;
        padding: 0.5rem 1rem;
    }
    
    .large-button button {
        font-size: 18px;
        padding: 1rem 2rem;
    }
    
    /* Disabled Button */
    .disabled-button button {
        opacity: 0.6;
        cursor: not-allowed;
    }
    
    .disabled-button button:hover {
        transform: none;
        box-shadow: none;
    }
    
    /* Result Boxes */
    .result-box {
        margin-top: 24px;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        font-family: 'Space Grotesk', sans-serif;
        letter-spacing: 0.5px;
    }
    
    .real-result {
        background-color: rgba(16, 185, 129, 0.2);
        border: 1px solid var(--success-color);
        color: var(--success-color);
    }
    
    .fake-result {
        background-color: rgba(239, 68, 68, 0.2);
        border: 1px solid var(--error-color);
        color: var(--error-color);
    }
    
    /* Spinner */
    .stSpinner > div > div {
        border-top-color: var(--accent-primary);
    }
    
    /* Code elements */
    code, pre, .code {
        font-family: 'Roboto Mono', monospace;
        font-size: 14px;
        background-color: var(--bg-elevated);
        border-radius: 4px;
        padding: 2px 5px;
    }
    
    /* Title and Subtitle */
    .title {
        font-size: 32px;
        font-weight: 700;
        font-family: 'Manrope', sans-serif;
        color: var(--text-primary);
        margin-bottom: 8px;
        text-align: center;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        font-size: 18px;
        font-family: 'IBM Plex Sans', sans-serif;
        color: var(--text-secondary);
        margin-bottom: 24px;
        text-align: center;
        line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

def render_header(active_page="Home"):
    """Render the header with navigation using Streamlit components"""
    # Add CSS for the header
    st.markdown("""
    <style>
    /* Adjust the main content to make room for our navigation */
    .main-content {
        margin-top: 20px !important;
    }
    
    /* Style for the header container */
    .header-container {
        background-color: var(--bg-secondary);
        padding: 15px 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    /* Reset all column styles */
    [data-testid="column"] {
        padding: 0 !important;
    }
    
    /* Style for the logo */
    .logo-text {
        font-size: 24px;
        font-weight: 700;
        font-family: 'Space Grotesk', sans-serif;
        color: var(--accent-primary);
        text-align: left;
        letter-spacing: 0.5px;
    }
    
    /* Navigation styles */
    .nav-button {
        width: 100%;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 14px;
        color: var(--text-secondary);
        background: transparent;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        padding: 0;
        margin: 0;
        letter-spacing: 0.2px;
    }
    
    .nav-button:hover {
        color: var(--text-primary);
        background: rgba(255, 255, 255, 0.1);
    }
    
    .nav-button.active {
        font-weight: 600;
        color: white;
        background-color: var(--accent-primary);
    }
    
    /* Fix for Streamlit button styling */
    div[data-testid="stButton"] {
        width: 100%;
    }
    
    div[data-testid="stButton"] > button {
        width: 100% !important;
        height: 36px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        color: var(--text-secondary) !important;
        background: transparent !important;
        border: none !important;
        border-radius: 6px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        padding: 0 !important;
        margin: 0 !important;
        letter-spacing: 0.2px !important;
        box-shadow: none !important;
    }
    
    div[data-testid="stButton"] > button:hover {
        color: var(--text-primary) !important;
        background: rgba(255, 255, 255, 0.1) !important;
        transform: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create a container for the header
    with st.container():
        # Create a row with logo on left and navigation on right
        col_logo, col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([4, 0.8, 0.8, 0.8, 0.8])
        
        # Logo on the left
        with col_logo:
            st.markdown('<div class="logo-text">Fake News Detector</div>', unsafe_allow_html=True)
        
        # Home button
        with col_nav1:
            if active_page == "Home":
                st.markdown('<button class="nav-button active">Home</button>', unsafe_allow_html=True)
            else:
                if st.button("Home", key="nav_home", use_container_width=True):
                    st.switch_page("homepage.py")
        
        # Detector button
        with col_nav2:
            if active_page == "Detector":
                st.markdown('<button class="nav-button active">Detector</button>', unsafe_allow_html=True)
            else:
                if st.button("Detector", key="nav_detector", use_container_width=True):
                    st.switch_page("pages/front_app.py")
        
        # How It Works button
        with col_nav3:
            if active_page == "How It Works":
                st.markdown('<button class="nav-button active">How It Works</button>', unsafe_allow_html=True)
            else:
                if st.button("How It Works", key="nav_how", use_container_width=True):
                    st.switch_page("pages/how_it_works.py")
        
        # About button
        with col_nav4:
            if active_page == "About":
                st.markdown('<button class="nav-button active">About</button>', unsafe_allow_html=True)
            else:
                if st.button("About", key="nav_about", use_container_width=True):
                    st.switch_page("pages/about.py")
        
        st.markdown('</div>', unsafe_allow_html=True)

def styled_button(label, button_type="primary", key=None, on_click=None, args=None, kwargs=None, use_container_width=False, icon=None, size="medium", disabled=False):
    """
    Create a button with a custom style class
    
    Parameters:
    - label: The text to display on the button
    - button_type: The type of button (primary, secondary, success, warning, danger, ghost)
    - key: A unique key for the button
    - on_click: Function to call when the button is clicked
    - args: Arguments to pass to the on_click function
    - kwargs: Keyword arguments to pass to the on_click function
    - use_container_width: Whether to make the button fill its container
    - icon: Icon to display on the button (emoji or icon code)
    - size: Size of the button (small, medium, large)
    - disabled: Whether the button is disabled
    
    Returns:
    - The result of st.button (True if clicked, False otherwise)
    """
    # Create a container for the button with the custom class
    container = st.container()
    
    # Prepare the label with icon if provided
    display_label = f"{icon} {label}" if icon else label
    
    # Special case for the "Check if it's Fake or Real" button - add underline
    if "Check if it's Fake or Real" in label and key == "check_fake_real_btn":
        if icon:
            display_label = f"{icon} <u>{label}</u>"
        else:
            display_label = f"<u>{label}</u>"
    
    # Add size class
    size_class = ""
    if size == "small":
        size_class = "small-button"
    elif size == "large":
        size_class = "large-button"
    
    # Add disabled class
    disabled_class = "disabled-button" if disabled else ""

    
    # Create the button with the specified parameters
    with container:
        # Apply the custom class
        st.markdown(f'<div class="{button_type}-button {size_class} {disabled_class}">', unsafe_allow_html=True)
        
        # Create the button normally
        result = st.button(
            label=display_label,
            key=key,
            on_click=on_click,
            args=args,
            kwargs=kwargs,
            use_container_width=use_container_width,
            disabled=disabled
        )
        
        # Close the div
        st.markdown('</div>', unsafe_allow_html=True)
    
    return result

def render_footer():
    """Render the footer"""
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <strong>Binary Brains</strong> © 2025 | Made by UTS Students
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add CSS for the footer
    st.markdown("""
    <style>
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def start_content():
    """Start the main content area"""
    # Apply CSS to the container that will be returned
    st.markdown("""
    <style>
    /* Target the next container that will be created */
    .main-content-wrapper > div {
        background-color: var(--bg-secondary);
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        padding: 30px;
        margin: 30px auto 100px auto;
        max-width: 1200px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create a div with a class that we can target with CSS
    st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)
    
    # Return the container that will hold the content
    return st.container()

def end_content():
    """End the main content area"""
    st.markdown('</div>', unsafe_allow_html=True)