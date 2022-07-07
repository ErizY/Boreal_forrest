import ee
import json
import streamlit as st

service_account = 'cep-eo@ee-mazy.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, key_data=json.dumps({
  "type": st.secrets["type"],
  "project_id": st.secrets["project_id"],
  "private_key_id": st.secrets["private_key_id"],
  "private_key": st.secrets["private_key"],
  "client_email": st.secrets["client_email"],
  "client_id": st.secrets["client_id"],
  "auth_uri": st.secrets["auth_uri"],
  "token_uri": st.secrets["token_uri"],
  "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
  "client_x509_cert_url": st.secrets["client_x509_cert_url"]
}))
ee.Initialize(credentials)

# get ASTER emissivity
aster = ee.Image("NASA/ASTER_GED/AG100_003")

# get ASTER FVC from NDVI
aster_ndvi = aster.select('ndvi').multiply(0.01)

aster_fvc = aster_ndvi.expression('((ndvi-ndvi_bg)/(ndvi_vg - ndvi_bg))**2',
                                  {'ndvi':aster_ndvi,'ndvi_bg':0.2,'ndvi_vg':0.86})
aster_fvc = aster_fvc.where(aster_fvc.lt(0.0),0.0);
aster_fvc = aster_fvc.where(aster_fvc.gt(1.0),1.0);
    
# bare ground emissivity functions for each band
def emiss_bare_band10(image):
    return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
        'EM':aster.select('emissivity_band10').multiply(0.001),
        'fvc':aster_fvc}).clip(image.geometry())

def emiss_bare_band11(image):
    return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
        'EM':aster.select('emissivity_band11').multiply(0.001),
        'fvc':aster_fvc}).clip(image.geometry())

def emiss_bare_band12(image):
    return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
        'EM':aster.select('emissivity_band12').multiply(0.001),
        'fvc':aster_fvc}).clip(image.geometry())

def emiss_bare_band13(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band13').multiply(0.001),
    'fvc':aster_fvc}).clip(image.geometry())

def emiss_bare_band14(image):
  return image.expression('(EM - 0.99*fvc)/(1.0-fvc)',{
    'EM':aster.select('emissivity_band14').multiply(0.001),
    'fvc':aster_fvc}).clip(image.geometry())
