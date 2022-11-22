# %%writefile app.py
import streamlit as st
from streamlit_option_menu import option_menu

# horizontal menu
selected = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "Home":
  st.write("You are at home")

if selected == "Upload":
  st.write("You are at Upload")

if selected == "Tasks":
  st.write("You are at tasks")

if selected == "Settings":
  st.write("You are at settings")
