
import geemap.foliumap as geemap
import ee
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
import os.path
import pickle as pkle
import streamlit.components.v1 as components
st.set_page_config(
    page_title="HOME",
    page_icon="	🏠",
    layout="wide",
)



header = st.container()
body = st.container()
footer = st.container()

components.html("""<h1 style="text-align: center; color:#33ff33; font-size:50px; ">Exploring the Boreal Forest through satellite data</h1>"""
)
col1, col2, col3 = st.columns([10,30,10])


with col2:
    image = Image.open('images/Boreal.png')
    st.image(image, caption="The Scale of the Boreal Forest", output_format="auto")

    




    st.markdown("""<dl style="color:#ffff;  font-family: Arial;>
Fire behaviour is changing worldwide, which is directly related to the planet's heating by human-caused climate change.
 
So, we asked what this means for the planet's most inhospitable, enormous and life giving forest - the Boreal/Taiga. It takes up the entire top of Earth, is rich with animal and plant diversity and, due to the harsh winters, is sparsely populated by people.


As fire activity is linked to dryness, we look at the Boreal/Taiga Forest to consider the history of Earth greatest remaining forest 

Making this exploration with Big Data to view Landscape Fire began as a desire to communicate the scale of the boreal forest and its role within the Earth System. We began asking questions about the transition from the historical fire regime in its primary regenerative capacity into the potential for the large parts of the forest to collapse from worsening fire and what impact that would have on the neighbouring systems such as the Gulf Stream or Artic Ice Shelf. Also, although fire is often reported in the Amazon, Australia, East Coast America and part of south and central Europe, fires activity in Boreal/Tiaga is seldom reported unless it comes into contact with a township, which was the case for Fort McMurray in 2016 and more recently in Lytton 2021 and 2022.

In the context of an accelerated transitioning out of the Holocene climate into something unknown, Fire imagery is now prevalent in news media, acting as a terrifying symbol of the threshold that has been crossed. Far from accepting this as a new normal, we have created this open-source platform for public use and your questions and independent exploration.


“The IPCC report says the future is going to be hotter - how hot, as the New York Times says, is up to us”. - Nov 28, 2021, Pyrocologist Professor David Bowman. </dl>
	
    
    
    
    """, unsafe_allow_html=True)
    
  



    components.html("""<h3 style="text-align: center; line-height:100px font: Arial; color:#33ff33; font-size:50px; ">About this website</h3>"""
    )
    

    st.markdown("""
            <dl style="color:#ffff;  font-family: Arial; ">
            <dd style="color:#ffff;  font-family: Arial; s">This website was created by Eriz Yusuf and Mohammed Mazy under Alan McFetrdige Photography, 
            The purpose of this website is to Show the scale of the Boreal Forest and help users understand what happens in this particular biome, this website is an informative website that is used to inform users of fires happening in and around the Boreal. This is still a work in progress so some data may not be avaliable and some features may not work as expected
            The data was taken from Various sources please see <a href="https://pastebin.com/1aHFFYy5">Boreal Forest Fires <a/> Sattleite imagery was taken From Nasa and the European space agency using Google earth engine</dd>
            </dl>


           

            """, unsafe_allow_html=True
            )
st.markdown('###')
st.markdown('###')
st.markdown('###')
st.markdown('###')
st.markdown('###')
st.markdown('###')

button_1, button_2 = st.columns([1,1])


with button_1:
    if st.button("Continue to Boreal_Exploration"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)


with button_2:
    if st.button("How to use "):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)
