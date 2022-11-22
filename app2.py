import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser

st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon=":tada:")

selected = option_menu(None, ["Home", "How to use", "Analyze", 'Contact Us'], 
    icons=['house', 'question-circle', "twitter", 'envelope'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "Home":
    st.title("Twitter Sentiment Analysis")
    st.subheader("Hey there!!! :wave: Welcome to our service")

    st.subheader("Wondering what we do?")
    st.markdown("We **_analyze_** the tweets for you guys to")
    st.write("1. Clear your doubts\n 2. Authenticity of rumors\n 3. Give you a topic for your gossips\n 4. Help in your philosophical research\n and much more!!!")

if selected == "How to use":
    st.title("You entered how to use")

if selected == "Analyze":
    genre = st.radio("What do you want to do",
                     ('I want to analyze the tweets from a twitter account', 'I want to analyze a topic', 'I want to analyze my dataset'))
    
    if genre == "I want to analyze the tweets from a twitter account":
        st.write("You will be redirected to another website.\n Please [Click Here >](https://project-se-ts-1.streamlit.app/)")
#         st.write("Please [Click Here >](https://project-se-ts-1.streamlit.app/)")
