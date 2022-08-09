import geemap.foliumap as geemap
import ee
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import time
import plotly.express as px

st.set_page_config(
    page_title="How to Use",
    page_icon="	",
    layout="wide"
)
AirQuality_monthspan = pd.read_csv('Data/filtered_df.csv')
AirQuality_before_and_after = pd.read_csv('Data/beforeandafter_df.csv')
AirQuality_yearSpan = pd.read_csv('Data/Year_spanDF.csv')


 
st.markdown(
            """<p style="color:#33ff33; font-size:50px;text-align:center">
            How to use the website</p>""",
            unsafe_allow_html=True,
        )
col1, col2,col3= st.columns((1,2,2))
with col1:
    Original = Image.open('images/Toolbar.png')
    st.image(Original)




with col2:

    st.text('')

    st.markdown("""

	-Camera Icon: Clicking this icon allows you to download a PNG of the graph selected(***If you use this tool please creadit us!***)

	-Magnifine glass: This tool allows you to select a specific area on the charts and zoom into it(**Note:** ***This only works on Bar charts and line graphs***)

	-Box: This tool allows you to zoom in and out of the graph

	-Plus and Minus: This allows you to zoom in and out of the graph

	-House: If you make a mistake or zoom in too far this tool allows you to reset axis to default
	""")



    



line1 = px.line(AirQuality_monthspan, x='date', y=AirQuality_monthspan.columns[1:5])
st.write(line1)
st.markdown("""Test each tool above to get a feel of how each tool works on the visulisation displayed""")

if st.button("Back to Home"):
        st.markdown('<meta http-equiv="refresh" content="0;url=/">', unsafe_allow_html=True)
