from pickle import TRUE
import geemap.foliumap as geemap
import ee
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
import plotly.express as px
import base64 
import streamlit.components.v1 as components

st.set_page_config(
    page_title="How to Use",
    page_icon="	",
    layout="wide"
)
AirQuality_monthspan = pd.read_csv('Data/filtered_df.csv')
AirQuality_before_and_after = pd.read_csv('Data/beforeandafter_df.csv')
AirQuality_yearSpan = pd.read_csv('Data/Year_spanDF.csv')


 
components.html(
            """<h1 style="color:#24851A; font-size:50px;text-align:center; font-family:"Times New Roman";">
            How to Use the Tool</h1>"""
        )

st.markdown(""">
<!DOCTYPE html>
<title>Text Example</title>
<style>
div.container {

}
div.container p {
font-family: Times;
font-style: normal;
font-weight: normal;
text-decoration: none;
text-transform: none;


</style>

<div class="container">
<p>This is our first version of the tool and there is many more updates to come!. If you have any feedback, thoughts, bugs email us at studio@alan-mcfetridge.com and we'd be happy to help!</p>
</div>
""", unsafe_allow_html=True)



st.markdown('***') 
toolbar = Image.open('images/Toolbar.png')
graph1,text1 = st.columns(2)
graph2,text2 = st.columns(2)
graph3,text3 = st.columns(2)
with graph1:
    for i in range(6):
        st.write("")
    
    image = Image.open('images/Toolbar.png')
    st.image(image, caption=None, width=500, use_column_width=250, clamp=False, channels="RGB", output_format="auto")
    
with text1:
    st.markdown("""
	
<!DOCTYPE html>
<title>Text Example</title>
<style>
div.container {

}
div.container p {
font-family: Times;
font-style: normal;
font-weight: normal;
text-decoration: none;
text-transform: none;


</style>

<div class="container">
<p>- Camera Icon: Clicking this icon allows you to download a PNG of the graph selected (<strong>If you use this tool please credit us!</strong>)
</p>
<p></p>
<p>- Magnifying Glass: This tool allows you to select a specific area on the charts and zoom into it (<strong>Note:This only works on bar charts and line graphs</strong>)
</p>
<p></p>
<p>- Box:This tool allows you to zoom in and out of the graph</p>
<p></p>
<p>- Plus and Minus: This allows you to zoom in and out of the graph</p>
<p></p>
<p>- House: If you make a mistake or zoom in too far this tool allows you to reset axis to default</p>
</div>""", unsafe_allow_html=True)
    




with graph2:

    line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:6])
    st.write(line1)
    st.caption("This Graph shows the air quality levels from Fort Mcmurray in the month of May 2016, Particulate Matter,Nitrogen Dioxide, Sulphur Dioxide and Carbon Monoxide")    

with text2:

    for i in range(12):
        st.write("")
    
    st.markdown("""
<!DOCTYPE html>
<title>Text Example</title>
<style>
div.container {

}
div.container p {
font-family: Times;
font-style: normal;
font-weight: normal;
text-decoration: none;
text-transform: none;


</style>

<div class="container">
<p>Test each tool on the graph to get a feel of how each tool works on the visualisation displayed</p>
</div>""",
    unsafe_allow_html=True)

video_file = open('images/Tool_working.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.caption("Here is an example of how the tool works, In this example you can see me selecting a fire from the dataset, changing the layer to LST which is land surface tempreature and also selecting a date range, Air quality only works from data from 2017 onwards")


Button_1, button_2= st.columns([1,1])


with Button_1:
    if st.button("Back to Home"):
        st.markdown('<meta http-equiv="refresh" content="0;url=/home">',
                unsafe_allow_html=True)

with button_2:
        st.markdown("""
      <!DOCTYPE HTML>
<html lang="en">
<head>
 <style>
  a:link,a:visited {
   color: Blue;
   background-color: https://alan-mcfetridge.com/cep;
   text-decoration: none;
   target-new: none;
  }
  a:hover {
   color: #0000FF;
   background-color: #FFFFC0;
   text-decoration: underline;
   target-new: none;
  }
 </style>
</head>
<body>
 <!-- Text link tag - by www.rapidtables.com -->
 <a href="https://alan-mcfetridge.com/cep">Return Centre for Ecological Philosophy</a>
</body>
</html>
        
        """, unsafe_allow_html=True)