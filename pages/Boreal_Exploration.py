import geemap.foliumap as geemap
import ee
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
ee.Authenticate()


st.set_page_config(
    page_title="Page 2 ",
    page_icon="👋",
)
st.markdown(
            """<p style="color:#33ff33; font-size:50px; text-align:center">
            A Deeper Dive Into The Boreal Forrest</p>""",
            unsafe_allow_html=True,
        )


st.markdown('This page will allow users to interact with the map and select the data that we have avaliable ')

m = geemap.Map(location=[56.72769575738292, -111.3802457353699], zoom_start=16)


st_data = st_folium(m, width = 725)
if st.button("Continue to Boreal_Exploration Data exploration"):
     st.markdown('<meta http-equiv="refresh" content="0;url=/Boreal_Exploration_Continued">', unsafe_allow_html=True)
