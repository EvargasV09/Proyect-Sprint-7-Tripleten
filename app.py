import pandas as pd
import plotly.express as px
import streamlit as st
import nbformat as nbf

data = pd.read_csv('data/vehicles_us.csv')
hist_button = st.button("construir histograma")
disp_button = st.checkbox("construir diagrama de dispersion")
if hist_button:
    st.write("Construyendo histograma de precios de vehículos")
    fig  = px.histogram(data, x="odometer")   
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write("Construyendo diagrama de dispersion de precios de vehículos")
    fig  = px.scatter(data, x="odometer", y="price")   
    st.plotly_chart(fig, use_container_width=True)