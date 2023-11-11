import streamlit as st

#Layout
st.set_page_config(
    page_title="DenCity",
    layout="wide",
    initial_sidebar_state="expanded")

#Sidebar
with st.sidebar:
    st.image(
        "assets/logo.png",
    )


#Header
st.title('Welcome to DenCity')
st.subheader('*smart city, smart people, smart surveillance*')
st.divider()

#Body
st.image(
    "assets/artwork.png",
)

