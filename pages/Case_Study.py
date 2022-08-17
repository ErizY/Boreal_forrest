import geemap.foliumap as geemap
import ee
import numpy
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
from streamlit_folium import st_folium
import folium
from earth_observation_v1 import Fire
from io import StringIO
import json
import numpy as np
import streamlit.components.v1 as components
from pickle import TRUE
import plotly.express as px
import base64 

st.set_page_config(
    page_title=" Case Study",
    layout="wide"
)

AirQuality_monthspan = pd.read_csv('Data/filtered_df.csv')
AirQuality_before_and_after = pd.read_csv('Data/beforeandafter_df.csv')
AirQuality_yearSpan = pd.read_csv('Data/Year_spanDF.csv')

components.html(
            """<h1 style="color:#24851A; font-size:50px;text-align:center; font-family:"Times New Roman";">
            Case Study of Air Quality</h1>"""
        )


col1, col2, col3 = st.columns([10,30,10])

with col2:
    st.markdown("The data for this case Study was provided by Alberta State in Canada. In this section there are a series of graphs which show the various different values of air quality in and around Fort Mcmurray during the year of 2016. This was known as the Horse River fire")
    st.markdown("""


<!DOCTYPE html>
<html>
<head>
<title>
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h2{font-family:Times,serif;color#24851A;}
p {font-family:Times, serif;font-size:14px;font-style:normal;font-weight:normal;}
</style>
</head>
<body>
<h2 style="color:#24851A;text-align:center; font-family:"Times New Roman";">Key words</h2>
<p></p>
<p>PM - Particulate Matter contains microscopic solids or liquid droplets that are so small that they can be inhaled and cause serious health problems.</p>
<p>NO2  - Nitrogen Dioxide</p>
<p>SO2 - Sulphur Dioxide</p>
<p>CO - Carbon Monoxide</p>
<p></p>
</body>
</html>


""",unsafe_allow_html=True)
line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:6])
st.write(line1)
st.caption("This Graph shows the air quality levels from Fort Mcmurray in the month of May 2016, Particulate Matter,Nitrogen Dioxide, Sulphur Dioxide and Carbon Monoxide")

line2 = px.line(AirQuality_before_and_after, x='date',y=AirQuality_before_and_after.columns[1:6])
st.write(line2)
st.caption("This graph shows the air quality levels From Fort Mcmurray in the month of April 2016-May 2016, to show the correlation of before and after the fire")


line3 = px.line(AirQuality_yearSpan, x='date',y=AirQuality_yearSpan.columns[1:6])
st.write(line3)
st.caption("This Graph shows the air quality levels from Fort Mcmurray from April 2016-June 2021")


button_1, button_2,button_3,button_4 = st.columns([1,1,1,1])

with button_1:
    if st.button("Continue to How to Use"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)



with button_2:
        if st.button("Back to home"):
            st.markdown(
            '<meta http-equiv="refresh" content="0;url=/">', unsafe_allow_html=True)


with button_3:
    if st.button("Back to boreal Exploration"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)

with button_4:
        link = '[Back to Website](https://alan-mcfetridge.com)'
        st.markdown(link, unsafe_allow_html=True)