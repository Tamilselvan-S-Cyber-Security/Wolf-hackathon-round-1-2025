import streamlit as st

def apply_custom_styles():
    """
    Apply the cyberpunk/neon theme styles to the Streamlit app
    """
    st.markdown("""
    <style>
    /* Import Neo Brutalist fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');
    
    /* Global styles - Neo Brutalist Theme */
    .stApp {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
    }
    
    /* Override Streamlit default dark theme */
    .stApp > div {
        background-color: #f8f9fa !important;
    }
    
    .main .block-container {
        background-color: #f8f9fa !important;
    }
    
    /* Force light theme */
    body {
        background-color: #f8f9fa !important;
        color: #000000 !important;
    }
    
    html {
        background-color: #f8f9fa !important;
    }
    
    /* Override Streamlit dark theme elements */
    .stApp > div > div {
        background-color: #f8f9fa !important;
    }
    
    .stApp > div > div > div {
        background-color: #f8f9fa !important;
    }
    
    /* Force all containers to use light theme */
    .main .block-container,
    .main .block-container > div,
    .main .block-container > div > div {
        background-color: #f8f9fa !important;
        color: #000000 !important;
    }
    
    /* Override any dark theme classes */
    [data-testid="stApp"] {
        background-color: #f8f9fa !important;
    }
    
    [data-testid="stApp"] > div {
        background-color: #f8f9fa !important;
    }
    
    /* Ensure all text is black */
    .stApp * {
        color: #000000 !important;
    }
    
    /* Additional theme overrides */
    .stApp {
        background: #f8f9fa !important;
    }
    
    .stApp > div {
        background: #f8f9fa !important;
    }
    
    .stApp > div > div {
        background: #f8f9fa !important;
    }
    
    .stApp > div > div > div {
        background: #f8f9fa !important;
    }
    
    /* Force light theme on all elements */
    div[data-testid="stApp"] {
        background-color: #f8f9fa !important;
    }
    
    div[data-testid="stApp"] > div {
        background-color: #f8f9fa !important;
    }
    
    /* Override any remaining dark elements */
    .stApp, .stApp * {
        background-color: #f8f9fa !important;
        color: #000000 !important;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Login container - Neo Brutalist */
    .login-container {
        text-align: center;
        padding: 3rem 2rem;
        background-color: #ffffff;
        border-radius: 0;
        margin-bottom: 2rem;
        border: 6px solid #000000;
        box-shadow: 8px 8px 0px #000000;
        position: relative;
    }
    
    .neon-title {
        font-size: 4rem;
        font-weight: 900;
        color: #000000;
        text-shadow: 4px 4px 0px #ffc107;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        text-transform: uppercase;
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes brutalist-pulse {
        0%, 100% {
            text-shadow: 4px 4px 0px #ffc107;
        }
        50% {
            text-shadow: 6px 6px 0px #ffc107, 8px 8px 0px #000000;
        }
    }
    
    .subtitle {
        font-size: 1.8rem;
        color: #000000;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 0px #00d4aa;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .description {
        font-size: 1.2rem;
        color: #000000;
        margin-bottom: 2rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Authentication card - Neo Brutalist */
    .auth-card {
        background-color: #ffc107;
        padding: 2.5rem;
        border-radius: 0;
        border: 6px solid #000000;
        box-shadow: 8px 8px 0px #000000;
        margin: 2rem 0;
        position: relative;
    }
    
    /* Game header - Neo Brutalist */
    .game-header {
        background-color: #00d4aa;
        padding: 2rem;
        border-radius: 0;
        border: 6px solid #000000;
        box-shadow: 6px 6px 0px #000000;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .user-info {
        color: #000000;
        font-size: 1.3rem;
        margin: 0;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Health score display - Neo Brutalist */
    .health-score {
        background-color: #ffeb3b;
        padding: 1.5rem;
        border-radius: 0;
        border: 6px solid #000000;
        text-align: center;
        box-shadow: 6px 6px 0px #000000;
        position: relative;
    }
    
    .health-score h3 {
        color: #000000;
        margin-bottom: 0.5rem;
        font-size: 1.4rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .score-display {
        font-size: 2.5rem;
        font-weight: 900;
        color: #000000;
        text-shadow: 3px 3px 0px #ffc107;
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Challenge containers - Neo Brutalist */
    .challenges-container {
        background-color: #f8f9fa;
        padding: 2.5rem;
        border-radius: 0;
        border: 8px solid #000000;
        box-shadow: 12px 12px 0px #000000;
        position: relative;
    }
    
    /* Challenge cards - Neo Brutalist */
    .challenge-card-easy {
        background-color: #00d4aa;
        padding: 2rem;
        border-radius: 0;
        border: 5px solid #000000;
        margin-bottom: 1.5rem;
        transition: all 0.2s ease;
        box-shadow: 6px 6px 0px #000000;
        position: relative;
    }
    
    .challenge-card-medium {
        background-color: #ffeb3b;
        padding: 2rem;
        border-radius: 0;
        border: 5px solid #000000;
        margin-bottom: 1.5rem;
        transition: all 0.2s ease;
        box-shadow: 6px 6px 0px #000000;
        position: relative;
    }
    
    .challenge-card-hard {
        background-color: #ffeb3b;
        padding: 2rem;
        border-radius: 0;
        border: 5px solid #000000;
        margin-bottom: 1.5rem;
        transition: all 0.2s ease;
        box-shadow: 6px 6px 0px #000000;
        position: relative;
    }
    
    .challenge-card-easy:hover,
    .challenge-card-medium:hover,
    .challenge-card-hard:hover {
        transform: translate(-2px, -2px);
        box-shadow: 8px 8px 0px #000000;
    }
    
    .challenge-card-easy.completed {
        background-color: #4caf50;
        border-color: #000000;
        box-shadow: 8px 8px 0px #000000;
    }
    
    .challenge-card-medium.completed {
        background-color: #ff9800;
        border-color: #000000;
        box-shadow: 8px 8px 0px #000000;
    }
    
    .challenge-card-hard.completed {
        background-color: #ff9800;
        border-color: #000000;
        box-shadow: 8px 8px 0px #000000;
    }
    
    .challenge-card-easy.locked,
    .challenge-card-medium.locked,
    .challenge-card-hard.locked {
        opacity: 0.6;
        background-color: #9e9e9e;
        border-color: #000000;
        box-shadow: 3px 3px 0px #000000;
    }
    
    .challenge-status {
        margin-top: 1rem;
        padding: 0.8rem;
        border-radius: 0;
        text-align: center;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        border: 3px solid #000000;
        background-color: #ffffff;
        box-shadow: 3px 3px 0px #000000;
    }
    
    /* Hint cost display - Neo Brutalist */
    .hint-cost {
        background-color: #ffc107;
        padding: 1.5rem;
        border-radius: 0;
        border: 4px solid #000000;
        text-align: center;
        box-shadow: 4px 4px 0px #000000;
    }
    
    /* Custom button styles - Neo Brutalist */
    .stButton > button {
        background-color: #ffeb3b;
        color: #000000;
        border: 4px solid #000000;
        border-radius: 0;
        padding: 1rem 2rem;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 1.1rem;
        transition: all 0.2s ease;
        box-shadow: 6px 6px 0px #000000;
        cursor: pointer;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stButton > button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 8px 8px 0px #000000;
        background-color: #ffc107;
    }
    
    /* Additional button styling for all button types */
    button, .stButton button, input[type="button"], input[type="submit"] {
        background-color: #ffeb3b !important;
        color: #000000 !important;
        border: 4px solid #000000 !important;
        border-radius: 0 !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        box-shadow: 6px 6px 0px #000000 !important;
    }
    
    button:hover, .stButton button:hover, input[type="button"]:hover, input[type="submit"]:hover {
        background-color: #ffc107 !important;
        transform: translate(-2px, -2px) !important;
        box-shadow: 8px 8px 0px #000000 !important;
    }
    
    /* Override any Streamlit button styling */
    .stButton > button:first-child {
        background-color: #ffeb3b !important;
        color: #000000 !important;
    }
    
    .stButton > button:first-child:hover {
        background-color: #ffc107 !important;
    }
    
    /* Input field styles - Neo Brutalist */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background-color: #ffffff;
        border: 4px solid #000000;
        border-radius: 0;
        color: #000000;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        padding: 1rem;
        box-shadow: 3px 3px 0px #000000;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #ffc107;
        box-shadow: 5px 5px 0px #ffc107;
        outline: none;
    }
    
    /* File uploader styles - Neo Brutalist */
    .stFileUploader > div {
        background-color: #f8f9fa;
        border: 4px dashed #000000;
        border-radius: 0;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 4px 4px 0px #000000;
    }
    
    /* Success and error messages - Neo Brutalist */
    .stSuccess {
        background-color: #4caf50;
        border: 4px solid #000000;
        border-radius: 0;
        box-shadow: 4px 4px 0px #000000;
        color: #000000;
        font-weight: 800;
    }
    
    .stError {
        background-color: #ffeb3b !important;
        border: 4px solid #000000 !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0px #000000 !important;
        color: #000000 !important;
        font-weight: 800 !important;
        padding: 1rem !important;
    }
    
    .stError > div {
        color: #000000 !important;
        font-weight: 800 !important;
    }
    
    .stError p {
        color: #000000 !important;
        font-weight: 800 !important;
        margin: 0 !important;
    }
    
    /* Streamlit error message specific styling */
    div[data-testid="stAlert"] .stError {
        background-color: #ffeb3b !important;
        border: 4px solid #000000 !important;
        color: #000000 !important;
    }
    
    div[data-testid="stAlert"] .stError * {
        color: #000000 !important;
        font-weight: 800 !important;
    }
    
    /* Additional error message styling */
    .stAlert .stError {
        background-color: #ffeb3b !important;
        border: 4px solid #000000 !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0px #000000 !important;
        color: #000000 !important;
        font-weight: 800 !important;
    }
    
    .stAlert .stError * {
        color: #000000 !important;
        font-weight: 800 !important;
    }
    
    /* Ensure all error message text is black and bold */
    .stError,
    .stError div,
    .stError span,
    .stError p,
    .stError strong,
    .stError b {
        color: #000000 !important;
        font-weight: 800 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Override any Streamlit default error styling */
    [data-testid="stAlert"] .stError,
    [data-testid="stAlert"] .stError * {
        background-color: #ffeb3b !important;
        color: #000000 !important;
        font-weight: 800 !important;
        border: 4px solid #000000 !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0px #000000 !important;
    }
    
    /* Specific styling for authentication error messages */
    .stError:contains("Authentication failed"),
    .stError:contains("INVALID_LOGIN_CREDENTIALS") {
        background-color: #ffeb3b !important;
        color: #000000 !important;
        font-weight: 800 !important;
        border: 4px solid #000000 !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0px #000000 !important;
        padding: 1rem !important;
    }
    
    /* Force all error message text to be black */
    .stError {
        color: #000000 !important;
    }
    
    .stError * {
        color: #000000 !important;
    }
    
    /* Ensure all text elements are black */
    body, html, .stApp, .stApp * {
        color: #000000 !important;
    }
    
    /* Override any remaining white text */
    * {
        color: #000000 !important;
    }
    
    /* Specific overrides for common elements */
    p, span, div, h1, h2, h3, h4, h5, h6, a, button, input, textarea, select {
        color: #000000 !important;
    }
    
    .stWarning {
        background-color: #ffeb3b;
        border: 4px solid #000000;
        border-radius: 0;
        box-shadow: 4px 4px 0px #000000;
        color: #000000;
        font-weight: 800;
    }
    
    .stInfo {
        background-color: #2196f3;
        border: 4px solid #000000;
        border-radius: 0;
        box-shadow: 4px 4px 0px #000000;
        color: #000000;
        font-weight: 800;
    }
    
    /* Dialog styles - Neo Brutalist */
    .stDialog {
        background-color: #ffffff;
        border: 6px solid #000000;
        border-radius: 0;
        box-shadow: 8px 8px 0px #000000;
    }
    
    /* Sidebar styles - Neo Brutalist */
    .css-1d391kg {
        background-color: #f8f9fa;
        border-right: 4px solid #000000;
    }
    
    /* Multiselect styles - Neo Brutalist */
    .stMultiSelect > div {
        background-color: #ffffff;
        border: 4px solid #000000;
        border-radius: 0;
        box-shadow: 3px 3px 0px #000000;
    }
    
    /* Remove default Streamlit padding - Neo Brutalist */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #f8f9fa;
    }
    
    /* Scrollbar styling - Neo Brutalist */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f8f9fa;
        border: 2px solid #000000;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #000000;
        border-radius: 0;
        border: 2px solid #ffc107;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #ffc107;
    }
    
    /* Neo Brutalist Additional Elements */
    .login-container::before {
        content: '';
        position: absolute;
        top: -4px;
        left: -4px;
        right: -4px;
        bottom: -4px;
        background: #ffc107;
        z-index: -1;
    }
    
    .auth-card::before {
        content: '';
        position: absolute;
        top: -4px;
        left: -4px;
        right: -4px;
        bottom: -4px;
        background: #000000;
        z-index: -1;
    }
    
    .game-header::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 20px;
        height: 20px;
        background: #000000;
        transform: rotate(45deg);
        transform-origin: center;
    }
    
    .challenge-card-easy::before,
    .challenge-card-medium::before,
    .challenge-card-hard::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 20px solid #000000;
        border-bottom: 20px solid transparent;
    }
    
    /* Brutalist typography enhancements */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -0.02em;
    }
    
    p, span, div {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
    }
    
    /* Raw, unpolished elements */
    .brutalist-accent {
        position: relative;
    }
    
    .brutalist-accent::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 100%;
        height: 4px;
        background: #ffc107;
        transform: skew(-15deg);
    }
    </style>
    """, unsafe_allow_html=True)
