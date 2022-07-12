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
# ee.Authenticate()

st.set_page_config(layout="wide")

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
            .css-18e3th9 {
                    padding-top: 3rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
            .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

AirQuality_monthspan = pd.read_csv('Data/filtered_df.csv')
AirQuality_before_and_after = pd.read_csv('Data/beforeandafter_df.csv')
AirQuality_yearSpan = pd.read_csv('Data/Year_spanDF.csv')

st.session_state["errors"] = []

df = pd.read_csv("Data/wildfire_boreal_forest.csv")
fires_choices = df["name"]
layers_choices = {"True Color": "true", "False Color": "false",
                  "SWIR": "swir", "NBR": "nbr", "BAI": "bai",
                  "EVI": "evi", "Air Quality (Nitrogen Dioxide)": "no2",
                  "Air Quality (Carbon Monoxide)": "co",
                  "LST": "lst"}

st.markdown(
            """<p style="color:#33ff33; font-size:50px; text-align:center">
            The Boreal Forrest Exploration</p>""",
            unsafe_allow_html=True,
        )

with st.sidebar:
    fire = st.selectbox("Choose a fire", fires_choices)
    st.session_state['fire_name'] = fire

    st.write("____________________")
    start_date = str(st.date_input("Start Date",
                                value=datetime.datetime.strptime(df[df['name'] == fire]["date_start"].iloc[0], "%d/%m/%Y").date(),
                                min_value=datetime.date(2000, 1, 1),
                                max_value=datetime.date.today()))

    end_date=str(st.date_input("End Date",
                                value=datetime.datetime.strptime(df[df['name'] == fire]["date_end"].iloc[0], "%d/%m/%Y").date(),
                                min_value = datetime.date(2000, 1, 1),
                                max_value = datetime.date.today()))

    st.write("____________________")

    layer=st.selectbox("Choose a layer", layers_choices.keys())

    if "Air Quality" in layer and pd.to_datetime(start_date) < pd.to_datetime('2017-11-13'):
            st.markdown(
                """<p class="small-font" style="color:red">
                    Air Quality layer unavailable before 2017-11-13.</p>""",
                unsafe_allow_html=True,
            )
            st.session_state["errors"].append(True)

    st.write("____________________")

    pressed=st.button("Build Map")


graph_1, map_1 = st.columns(2)
graph_2, map_2 = st.columns(2)


with graph_1:
	line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:5])
	st.write(line1)
    

with graph_2:
	line2 = px.line(AirQuality_before_and_after, x='date', y=AirQuality_before_and_after.columns[1:5])
	st.write(line2)


prev, _ ,next = st.columns([1, 10, 1])




with map_1:
    m = geemap.Map(location=[56.72769575738292, -111.3802457353699], zoom_start=10)
    m.to_streamlit(
            width=1000, height=500)

with map_2:
    m = geemap.Map(location=[56.72769575738292, -111.3802457353699], zoom_start=10)
    m.to_streamlit(
            width=1000, height=500)



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
