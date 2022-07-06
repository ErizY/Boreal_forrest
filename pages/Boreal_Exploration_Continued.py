import geemap.foliumap as geemap
import ee
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
import plotly.express as px
import time
from streamlit_folium import st_folium
import folium
import os.path
import pickle as pkle
ee.Authenticate()

st.set_page_config(layout="wide")

AirQuality_monthspan = pd.read_csv('Data/filtered_df.csv')
AirQuality_before_and_after = pd.read_csv('Data/beforeandafter_df.csv')
AirQuality_yearSpan = pd.read_csv('Data/Year_spanDF.csv')

st.markdown(
            """<p style="color:#33ff33; font-size:50px; text-align:center">
            The Boreal Forrest Exploration</p>""",
            unsafe_allow_html=True,
        )
graph_1, graph_2, graph_3 = st.columns(3)



with graph_1:
	line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:5])
	st.write(line1)

with graph_2:
	line2 = px.line(AirQuality_before_and_after, x='date', y=AirQuality_before_and_after.columns[1:5])
	st.write(line2)


prev, _ ,next = st.columns([1, 10, 1])



m = geemap.Map(location=[56.72769575738292, -111.3802457353699], zoom_start=10)


st_data = st_folium(m, width = 400)



button_1, button_2, button_3 = st.columns(3)


with button_1:
    if st.button("Back to Boreal_Exploration"):
         st.markdown('<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)

with button_2:
    if st.button("View data and extra information on fire"):
        st.markdown('<meta http-equiv="refresh" content="0;url=/Boreal_Exploration_Continued">', unsafe_allow_html=True)



with button_3:
    if st.button("How to use "):
        st.markdown('<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)
