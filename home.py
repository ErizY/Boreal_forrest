
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


components.html("""

<meta name="viewport" content="width=device-width, initial-scale=1.0">

"""

)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

header = st.container()
body = st.container()
footer = st.container()

components.html("""<h1 style="text-align: center; color:#33ff33; font-size:50px; ">Exploring the Boreal Forest through satellite data</h1>"""
)
col1, col2, col3 = st.columns([10,30,10])


with col2:
    image = Image.open('images/Boreal.png')
    st.image(image, caption="The Scale of the Boreal Forest", width=1000, use_column_width=1000, clamp=False, channels="RGB", output_format="auto")

    
    components.html("""
    <ul style="color:#ffff;  font-family: Arial;">
	<li>The boreal forest is the worlds largest biome on planet earth!</li>
    <li>The forest zone consists of 8 countries which include:Canada,China,Finland,Japan,Russia,Norway,Sweden and the United States.It also covers some costal areas of Iceland, areas of Northern Kazakhstan, Estonia and the Scottish Highlands</li>
	<li>The Forest covers 17 million square kilometres (6.6 million square miles) or 11.5% of the earths land</li>
	<li>The largest areas of the forest are in Canada and Russia</li>
	<li>The fire season in the Boreal forest typically lasts from May to October with peaks of activity between July and August</li>
</ul>

""")


  

    st.markdown('---')

    components.html("""<h3 style="text-align: center; line-height:100px font: Arial; color:#33ff33; font-size:50px; ">About this website</h3>""",
    )
    
    st.markdown('###')
    
    components.html("""
            <dl style="color:#ffff;  font-family: Arial;">
            <dd style="color:#ffff;  font-family: Arial;">This website was created by Eriz Yusuf and Mohammed Mazy under Alan McFetrdige Photography, 
            The purpose of this website is to Show the scale of the Boreal Forest and help users understand what happens in this particular biome, this website is an informative website that is used to inform users of fires happening in and around the Boreal. This is still a work in progress so some data may not be avaliable and some features may not work as expected
            The data was taken from Various sources please see <a href="https://pastebin.com/1aHFFYy5">Boreal Forest Fires <a/> Sattleite imagery was taken From Nasa and the European space agency using Google earth engine</dd>
            </dl>


           

            """)

button_1, button_2 = st.columns([1,1])

with button_1:
    if st.button("Continue to Boreal_Exploration"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)


with button_2:
    if st.button("How to use "):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)
