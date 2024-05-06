import streamlit as st

# Set wide page configuration
st.set_page_config(layout="wide")

# Updated Embed URL for the PowerBI dashboard
powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiMTI3YWQ4MDEtZmU0OS00YWYxLTgzOGUtMDVjMGM3ZTg0Mzc4IiwidCI6IjM0YmQ4YmVkLTJhYzEtNDFhZS05ZjA4LTRlMGEzZjExNzA2YyJ9'

# HTML and CSS within Markdown to center the title and the iframe
html_code = f"""
<div style='text-align: center; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;'>
    <h1 style='margin-top: 0px;'>Myntra Sales Dashboard</h1>
    <iframe title="Myntra Sales Dashboard" width="1024" height="612" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
