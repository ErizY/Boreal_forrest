import geemap.foliumap as geemap
import ee
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
import os.path
import pickle as pkle

st.set_page_config(
    page_title="HOME",
    page_icon="	🏠",
    layout="wide"
)







with open('style.css') as f:
	st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

header = st.container()
body = st.container()
footer = st.container()



st.markdown(
            """<p style="color:#33ff33; font-size:50px; text-align:center">
            The Boreal Forrest</p>""",
            unsafe_allow_html=True,
        )











image = Image.open('images/placeholder-image.png')
st.image(image, caption='The scale of the Boreal Forrest')

st.markdown('This text is just to show the layout and how it would look on the actual system')


with st.expander("About"):
     st.write("""
         This website was created by Eriz Yusuf and Mohammed Mazy under Alan McFetrdige Photography, 
         The purpouse of this website..............

         the data was taken from.............
         the purpose of the data.........................

     """)

button_1, button_2, button_3 = st.columns(3)

with button_1:
    if st.button("Continue to Boreal_Exploration"):
         st.markdown('<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)

with button_2:
    if st.button("View data and extra information on fire"):
        st.markdown('<meta http-equiv="refresh" content="0;url=/Boreal_Exploration_Continued">', unsafe_allow_html=True)



with button_3:
    if st.button("How to use "):
        st.markdown('<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)
