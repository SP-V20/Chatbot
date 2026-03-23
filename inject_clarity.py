# inject_clarity.py
import streamlit.components.v1 as components
import os

def inject_clarity():
    """Inject Microsoft Clarity script into Streamlit app."""
    script_path = os.path.join(os.path.dirname(__file__), "clarity_script.html")
    
    with open(script_path, "r") as f:
        clarity_script = f.read()
    
    components.html(clarity_script, height=0, width=0)
