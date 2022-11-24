import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m4wmgweb.json")

lottie_coding1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qxmkn9ou.json")
    

selected = option_menu(None, ["Home", "How to use", "Analyze", 'Contact Us'], 
    icons=['house', 'question-circle', "twitter", 'envelope'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "Home":
    st.title("Twitter Sentiment Analysis")
    st.subheader("Hey there!!! :wave: Welcome to our service")
    
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Wondering what we do?")
            st.markdown("We **_analyze_** the tweets for you guys to")
            st.write("1. Clear your doubts\n 2. Authenticity of rumors\n 3. Give you a topic for your gossips\n 4. Help in your philosophical research\n and much more!!!")
        
        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")

if selected == "How to use":
    st.title("You entered how to use")

if selected == "Analyze":
    genre = st.radio("What do you want to do",
                     ('I want to analyze the tweets from a twitter account', 'I want to analyze a topic', 'I want to analyze my dataset'))
    
    if genre == "I want to analyze the tweets from a twitter account":
        st.write("You will be redirected to another website. Please [Click Here >](https://project-se-ts-1.streamlit.app/)")
        
    if genre == "I want to analyze a topic":
        st.write("You will be redirected to another website. Please [Click Here >](https://project-se-ts-3.streamlit.app/)")
        
    if genre == "I want to analyze my dataset":
        st.write("You will be redirected to another website. Please [Click Here >](https://project-se-ts-1.streamlit.app/)")

if selected == "Contact Us":
#     Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")
    with st.container():
        left_column, right_column = st.columns(2)
        with right_column:
            st_lottie(lottie_coding1, height=400, key="coding")
        st.write("---")
        st.header("Get In Touch With Us!")
        st.subheader("Feel free to ask anything")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/kbansal_be20@thapar.edu" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
