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

st.markdown("""<h1 style="text-align: center; color:#33ff33; font-size:50px; ">The Boreal Forest</h1>""",
    unsafe_allow_html=True,
)
col1, col2, col3 = st.columns(3)


with col2:
    image = Image.open('images/Boreal.png')
    st.image(image, caption='The scale of the Boreal Forest')

    st.markdown(
        """
        -The boreal forest is the worlds largest biome on planet earth! The forest zone consists of 8 countries: Canada,China,Finland,Japan,Russia,Norway,Sweden and the United States. It also coveres some costal areas of Iceland,areas of Northern Kazakhstan, Estonia and the Scottish Highlands
            
        -The Forrest covers 17 million square kilometers (6.6 million square miles) or 11.5% of the earths land

        -The largest areas of the forest are in Canda and Russia

        -The fire season in the Boreal forest typically lasts from May to October with peaks of activity between July and August
        
        
        
        
        """)

    with st.expander("About"):
        st.markdown("""
            This website was created by Eriz Yusuf and Mohammed Mazy under Alan McFetrdige Photography, 
            The purpose of this website is to Show the scale of the Boreal Forest and help users understand what happens in this particular biome, this website is an informative website that is used to inform users of fires happening in and around the Boreal. This is still a work in progress so some data may not be avaliable and some features may not work as expected

            The data was taken from Various sources please see: [Boreal forest Fires](https://pastebin.com/1aHFFYy5)

            Sattleite imagery was taken From Nasa and the European space agency using Google earth engine


           

            """)
button_1, button_2, button_3 = st.columns(3)

with button_1:
    if st.button("Continue to Boreal_Exploration"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)

with button_2:
    if st.button("View data and extra information on fire"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration_Continued">', unsafe_allow_html=True)


with button_3:
    if st.button("How to use "):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)
