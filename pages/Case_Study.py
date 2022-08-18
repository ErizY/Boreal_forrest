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
    st.markdown("""<!DOCTYPE html>
<html>
<head>
<!-- HTML Codes by Quackit.com -->
<title>
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}

p {font-family:Times;font-style:normal;font-weight:normal;}
</style>
</head>
<body>
<h1></h1>
<p>Here we draw attention to additional data from the 2016 Fort McMurray Fire (FMMF), which is the subject of the Centre of Ecological Philosophy's <a href="https://alan-mcfetridge.com/#/on-the-line/">first book </a> and <a href="https://alan-mcfetridge.com/#/song-of-the-dead/"> upcoming monograph </a>. The Air Quality Data is intriguing and alarming. In contrast, the photography reveals the stillness of the aftermath and the silence after a sudden change. But here, atmospheric data adds dimension to show how truly explosive the rising energy became. 
     </p>
<p></p>
<p>Alberta State in Canada provided the data for this case study. This section shows a series of graphs with air quality values in and around Fort McMurray during 2016.  
</p>
<p></p>
</body>
</html>

""", unsafe_allow_html=True)
with st.sidebar:
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
<h2 style="color:#24851A;text-align:center; font-family:"Times New Roman";">Key</h2>
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

st.markdown("""
<!DOCTYPE html>
<html>
<head>
<title>
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{font-family:Arial, sans-serif;}
p {font-family:Times, font-style:normal;font-weight:normal}
</style>
</head>
<body>
<h1></h1>
<p>The FMMF was a PyroCb or Pyrocumulonimbus Fire Storm. Up until the 1980s PyroCb’s were rare. However, in the past 40 years, they have begun to occur frequently on Earth. The FMMF case study shows a fundamental change in extreme fire behaviour and another reason why this fire registers as a significant turning point. </p>
<p></p>
<p>PyroCb storms funnel their smoke like a chimney into Earth's stratosphere, with lingering ill effects, which are noticed in the following graphs, and also reflected in the number of deaths from smoke inhalation at the time of fires, which adds unprecedented health costs to fire events.</p>

</body>
</html>


""" ,unsafe_allow_html=True)

line2 = px.line(AirQuality_before_and_after, x='date',y=AirQuality_before_and_after.columns[1:6])
st.write(line2)
st.caption("This graph shows the air quality levels From Fort Mcmurray in the month of April 2016-May 2016, to show the correlation of before and after the fire")

st.markdown("""

<!DOCTYPE html>
<html>
<head>

<title>
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
p {font-family:Times;font-style:normal;font-weight:normal;}
</style>
</head>
<body>
<h1></h1>
<p>David Bowman is the Professor of Pyrogeography and Fire Science at the University of Tasmania and the<a href="https://firecentre.org.au/"> Director of the Fire Centre</a> . We collaborated with David for <a href ="https://alan-mcfetridge.com/#/fire-in-australia/">‘Fire in Australia’</a>, and as a specialist on world fire, David’s description of PyrosCbs categorically links the sudden change in fire behaviour to human-caused Climate Change. </p>
<p></p>
<p></p>
<p>“ A PyroCb is basically, I would say, is the clenched fist of climate change. It's an absolute act of climate assertion. It's asserting itself. What do I mean by a clenched fist? Well, literally, clouds punch into the stratosphere ten or fifteen kilometres vertically, and these clouds are driven by extreme fire behaviour that generates so much energy and so much smoke that the latent energy in the water vapour and the smoke creates a heat engine that drives the smoke high, high into the sky and right up into the stratosphere and creates its own weather systems, it creates black hail, creates, lightning, creates, tornadoes and creates extremely dangerous and unpredictable fire behaviour.’ -  from   - Nov 28, 2021 <a href = "https://www.youtube.com/watch?v=Bu3-QGyVed0">“Fire Thinking, Fire Beings, and the End of the World as We Know It’</a></p>
<p></p>
</body>
</html>




""" ,unsafe_allow_html=True)


line3 = px.line(AirQuality_yearSpan, x='date',y=AirQuality_yearSpan.columns[1:6])
st.write(line3)
st.caption("This Graph shows the air quality levels from Fort Mcmurray from April 2016-June 2021")

st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')


button_1, button_2,button_3,button_4 = st.columns([1,1,1,1])

with button_1:
    if st.button("Continue to How to Use"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/How_to_Use">', unsafe_allow_html=True)



with button_2:
        if st.button("Back to Home"):
            st.markdown(
            '<meta http-equiv="refresh" content="0;url=/">', unsafe_allow_html=True)


with button_3:
    if st.button("Back to boreal Exploration"):
        st.markdown(
            '<meta http-equiv="refresh" content="0;url=/Boreal_Exploration">', unsafe_allow_html=True)

with button_4:
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
   color: https://alan-mcfetridge.com/cep;
   background-color: https://alan-mcfetridge.com/cep;
   text-decoration: underline;
   target-new: none;

  }
 </style>
</head>
<body>
 <!-- Text link tag - by www.rapidtables.com -->
 <a href="https://alan-mcfetridge.com/cep">Return to the Centre for Ecological Philosophy</a>
</body>
</html>
        
        """, unsafe_allow_html=True)
        
