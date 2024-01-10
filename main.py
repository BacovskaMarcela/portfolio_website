import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("Marcela Bačovská")
    content = """
    Hi, I'm Marcela! I'm an amateur Python enthusiast and data analyst. I've completed a long-term course at Czechitas 
    called the Digital Academy Data, and I'm currently seeking job opportunities in these fields. 
    I'm ready to learn anything!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)