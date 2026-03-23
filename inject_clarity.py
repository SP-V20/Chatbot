# inject_clarity.py
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def inject_clarity():
    project_id = os.getenv("CLARITY_PROJECT_ID", "w0e7bqjoub")

    clarity_script = f"""
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){{
            c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        }})(window, document, "clarity", "script", "{project_id}");
    </script>
    """
    st.markdown(clarity_script, unsafe_allow_html=True)
