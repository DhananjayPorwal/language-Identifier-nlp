import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl', 'rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Tool")
input_test = st.text_input("Enter your text here", "Welcome to Tech Ram")

button_clicked = st.button("Identify Language")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))