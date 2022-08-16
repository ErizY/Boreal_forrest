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
            """<h1 style="color:#33ff33; font-size:50px;text-align:center">
            How to use the Tool</h1>"""
        )

components.html("""<p style="color:#ffff; text-align:center; font-family: Arial; ">This is our first version of the tool and there is many more updates to come!. If you have any feedback, thoughts, bugs email us at studio@alan-mcfetridge.com and we'd be happy to help!.</p>
</p>
""")



st.markdown('***') 
toolbar = Image.open('images/Toolbar.png')
graph1,text1 = st.columns(2)
graph2,text2 = st.columns(2)
graph3,text3 = st.columns(2)
with graph1:
    for i in range(6):
        st.write("")
    
    image = Image.open('images/Toolbar.png')
    st.image(image, caption=None, width=1000, use_column_width=500, clamp=False, channels="RGB", output_format="auto")
    
with text1:
    st.markdown("""
	-Camera Icon: Clicking this icon allows you to download a PNG of the graph selected(***If you use this tool please creadit us!***)

	-Magnifine glass: This tool allows you to select a specific area on the charts and zoom into it(**Note:** ***This only works on Bar charts and line graphs***)

	-Box: This tool allows you to zoom in and out of the graph

	-Plus and Minus: This allows you to zoom in and out of the graph

	-House: If you make a mistake or zoom in too far this tool allows you to reset axis to default""")
    




with graph2:

    line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:5])
    st.write(line1)
    st.caption("This Graph shows the Air quality levels From Fort Mcmurray in the month of May 2016, Carbon Monoxide,Particulate matter and Nitrogen Dioxide")    

with text2:

    for i in range(12):
        st.write("")
    
    st.markdown("""<div style="text-align: center">Test each tool on the graph to get a feel of how each tool works on the visulisation displayed</div>""",
    unsafe_allow_html=True)

video_file = open('images/Tool_working.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.caption("Here is an example of how the tool works, In this example you can see me selecting a fire from the dataset, changing the layer to LST which is land surface tempreature and also selecting a date range, Air quality only works from data from 2017 onwards")
if st.button("Back to Home"):
    st.markdown('<meta http-equiv="refresh" content="0;url=/home">',
                unsafe_allow_html=True)