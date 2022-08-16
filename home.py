
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
    st.image(image, caption="The Scale of the Boreal Forest", output_format="auto", use_column_width='always')

    




    st.markdown("""
<!DOCTYPE html>
<title>Text Example</title>
<style>
div.container {
}
div.container p {
font-family: Arial;
font-style: normal;
font-weight: normal;
text-decoration: none;
text-transform: none;

}
</style>

<div class="container">
<p>Fire behaviour is changing worldwide. In general terms, landscape fires are occurring more often and becoming more severe. Being directly related to the planet's heating by human-caused climate change, we asked what this means for the planet's most inhospitable, enormous and life-giving forest - the Boreal/Taiga. The world's largest land biome makes its way around the entire top of Earth as a giant ring shape. Therefore it connects people from Europe, Asia and North America. It is rich with animal and plant diversity and, due to the harsh winters, is sparsely populated by people.</p>
<p></p>
<p>This tool provides an open-source exploration of the Boreal & Taiga to scan about and consider our relationship with the forest, which many of us benefit from in terms of air quality yet seldom see in our daily lives. We hope with this tool, you will be able to connect with it.</p>
<p></p>
</div>
	
    
    
    
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
