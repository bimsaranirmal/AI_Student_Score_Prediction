def get_css():
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global app style */
    .stApp {
        font-family: 'Outfit', sans-serif;
        background: radial-gradient(circle at top left, #1e1b4b, #0f172a, #020617);
        color: #e2e8f0;
    }

    /* Headers with gradient text */
    h1, h2, h3, h4 {
        font-weight: 700;
        background: linear-gradient(90deg, #c084fc, #6366f1, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* Glassmorphism Card style */
    .card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.3);
    }

    /* Section titles */
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        padding-left: 1rem;
        border-left: 4px solid #c084fc;
        background: linear-gradient(90deg, rgba(192, 132, 252, 0.1), transparent);
        padding: 0.5rem 1rem;
        border-radius: 0 8px 8px 0;
    }

    /* Input label colors */
    label, .stMultiSelect label, .stTextInput label, .stNumberInput label, .stSlider label {
        color: #94a3b8 !important;
        font-size: 0.9rem !important;
        font-weight: 500;
    }

    /* Input Fields (Text, Number, Select) */
    .stTextInput > div > div, .stNumberInput > div > div, .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.05);
        color: #f8fafc;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    .stTextInput > div > div:focus-within, .stNumberInput > div > div:focus-within, .stSelectbox > div > div:focus-within {
        border-color: #c084fc;
        box-shadow: 0 0 0 2px rgba(192, 132, 252, 0.2);
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #8b5cf6, #3b82f6);
        color: white;
        border-radius: 30px;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #7c3aed, #2563eb);
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6);
    }
    .stButton > button:active {
        transform: scale(0.98);
    }

    /* Success/info messages */
    .stInfo {
        background-color: rgba(59, 130, 246, 0.1);
        color: #bfdbfe;
        border-left: 4px solid #3b82f6;
    }
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1);
        color: #bbf7d0;
        border-left: 4px solid #22c55e;
    }
    .stError {
        background-color: rgba(239, 68, 68, 0.1);
        color: #fecaca;
        border-left: 4px solid #ef4444;
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #c084fc, #3b82f6, #06b6d4);
        border-radius: 10px;
    }

    /* Metric styling */
    .metric-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .metric-label {
        font-size: 1.1rem;
        color: #94a3b8;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(to bottom, #f8fafc, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 1rem;
        color: #64748b;
        font-size: 0.875rem;
        margin-top: 4rem;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.02);
        border-radius: 10px;
        color: #e2e8f0;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #0f172a;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

</style>
"""
