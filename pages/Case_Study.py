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
            Case Study of Air quality</h1>"""
        )


line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:5])
st.write(line1)
st.caption("This Graph shows the Air quality levels From Fort Mcmurray in the month of May 2016, Carbon Monoxide,Particulate matter and Nitrogen Dioxide")

line2 = px.line(AirQuality_before_and_after, x='date',y=AirQuality_before_and_after.columns[1:5])
st.write(line2)
st.caption("This Graph shows the Air quality levels From Fort Mcmurray in the month of April 2016-May 2016, to show the correlation of before and after the fire")


line3 = px.line(AirQuality_yearSpan, x='date',y=AirQuality_yearSpan.columns[1:5])
st.write(line3)
st.caption("This Graph shows the Air quality levels From Fort Mcmurray from April 2016-June 2021")


