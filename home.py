
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

components.html("""<h1 style="text-align: center; color:#24851A; font-size:50px; font:"Times New Roman"; ">Exploring the Boreal Forest through Satellite Data</h1>"""
)

st.markdown('***') 
col1, col2, col3 = st.columns([10,30,10])


with col2:
    image = Image.open('images/Boreal.jpg')
    st.image(image, caption="The Scale of the Boreal Forest - Prototype Boreal Map was created by Alan McFetridge, Eriz Yusuf, Mohammed Mazy, European Space Agency and the Centre of Ecological Philosophy. © 2022.", output_format="auto", use_column_width='always')

    




    st.markdown("""
<!DOCTYPE html>
<title>Text Example</title>
<style>
div.container {

}
div.container{
font-family: "Times New Roman";
font-style: normal;
font-weight: normal;
text-decoration: none;
text-transform: none;


</style>

<div class="container">
<p>Fire behaviour is changing worldwide. In general terms, landscape fires are occurring more often and becoming more severe. Being directly related to the planet's heating by human-caused climate change, we asked what this means for the planet's most inhospitable, enormous and life-giving forest - the Boreal/Taiga. The world's largest land biome makes its way around the entire top of Earth as a giant ring shape. Therefore it connects people from Europe, Asia and North America. It is rich with animal and plant diversity and, due to the harsh winters, is sparsely populated by people.</p>
<p></p>
<p>This tool provides an open-source exploration of the Boreal & Taiga to scan about and consider our relationship with the forest, which many of us benefit from in terms of air quality yet seldom see in our daily lives. We hope with this tool, you will be able to connect with it.</p>
<p></p>
<hr class="solid">
<h4 style="text-align: center; font-family:Times;color:#24851A;">5 Facts About The Boreal Forest</h4>

<p>- The forest zone consists of 8 countries which include: Canada, China, Finland, Japan, Russia, Norway, Sweden and the United States. It also covers some costal areas of Iceland, areas of Northern Kazakhstan, Estonia and the Scottish Highlands.</p>
<p></p>
<p>- Canada has 28% of the worlds Boreal Zone which acumilates to 552 million hectares.</p>
<p></p>
<p>- The Forest covers 17 million square kilometres (6.6 million square miles) or 11.5% of the earths land.</p>
<p></p>
<p>- The largest areas of the forest are in Canada and Russia.</p>
<p></p>
<p>- The fire season in the Boreal forest typically lasts from May to October with peaks of activity between July and August. Approximately  2 million hectares  of the forest burns at this time.</p>
</div>
    
    
    """, unsafe_allow_html=True)
    
  

    st.markdown('***') 

    components.html("""<h3 style="text-align: center; color:#24851A; font-size:50px; font:"Times New Roman" ">About this Tool</h3>"""
    )
    st.markdown('***') 
    
    st.markdown("""
<!DOCTYPE html>
<title>Text Example</title>
<style>
div.container {

}
div.container  {
font-family: "Times";
font-style: normal;
font-weight: normal;
text-decoration: none;
text-transform: none;


</style>

<div class="container">
<p>This Tool was created by Eriz Yusuf and Mohammed Mazy under Alan McFetrdige Photography. This was created with intention to spread awarness of the ongoing issues caused by the global warming crisis</p>
<p> This tool is used to make it aware that there are ongoing fires throughout the boreal forest on a seasonaly basis</p>
<p></p>
<p>-The Satellite data was provided by Nasa and ESA using the Google Earth Engine environment</p>
<p>-We gathered our information from <a href="https://pastebin.com/1aHFFYy5">Boreal Fires</a></p>
<p></p>
<p><strong>Satellites used in the tool Currently:</strong></p>
<p></p>
<p>Sentinel 2 - This satellite  has a resolution of 10m/pixel , it scans an area for 10 days at a time  so when exploring please consider that some areas may be missing or it will overlap.
try to use 2-4 day cycles for example the horse river fire began back in may 2016 so you could do the 2nd-4th of may and then see the results</p>
<p></p>
<p>LANDSAT 8 (LST) - This is the Temperature sensor which generates the heat-map , it cycles over 16 day cycles so you would need to have a larger date range selected 16-30 days works fine! </p>
<p></p>
<p>Sentinel 5p  - This is the Air quality sensory satellite currently we have Carbon Monoxide and Nitrogen Dioxide , Air Quality layer unavailable before 2017-11-13 it cycles over 14 days so 14+ days work fine!</p>
<p></p>
</div>


           

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
    if st.button("Continue to Boreal Exploration"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)


with button_2:
    if st.button("How to use "):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)
