
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
<p>Hello and welcome. We have made this open-source exploration of the Boreal & Taiga to develop an interest in how fire lives on the landscape and with people. This was created to spread awareness of the ongoing issues caused by the global heating crisis.
</p>
<p></p>
<p>We discovered that despite the forest's size and vital role in climate stability, few people know this. We felt that it would be great to bring some attention to fire activity and began writing code to enable free public exploration.
</p>
<p>Consider this vast region of life-giving ultimate beauty. Up north lays 11.5% of the Earth's surface, working away naturally all year around while we sleep. It makes me think of our lungs, yet it is also much like our heart and blood, moving and circulating without any thought or direction from us. When we consider the variety of unseen inter-relationships from air quality to commercial wood and oil in our daily lives, we hope with this tool, you will be able to connect with the source.</p>
<p>In the background of this exploration into an earthly wonderland is the seriousness of accelerated human-caused climate change. The IPCC Chair stated in June 2022, "We are not on track to achieve a climate-resilient sustainable world.” There is much work to do, and we hope this project can positively impact essential social and political change.</p>

<p></p>
<hr class="solid">
<h4 style="text-align: center; font-family:Times;color:#24851A;">5 Facts About The Boreal/Taiga Forest</h4>

<p>- The forest zone consists of 8 countries which include: Canada, China, Finland, Japan, Russia, Norway, Sweden and the United States. It also covers some costal areas of Iceland, areas of Northern Kazakhstan, Estonia and the Scottish Highlands.</p>
<p></p>
<p>- Canada has 28% of the worlds Boreal/Taiga Zone which conists of 552 million hectares.</p>
<p></p>
<p>- The Forest covers 17 million square kilometres (6.6 million square miles) or 11.5% of the earths land.</p>
<p></p>
<p>- The largest areas of the forest are in Canada and Russia.</p>
<p></p>
<p>- The fire season typically lasts from May to October with peaks of activity between July and August. Approximately 2 million hectares of the Canadian forest region burns at this time.</p>
</div>
    
    
    """, unsafe_allow_html=True)
   
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
