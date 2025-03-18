import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('notebooks/vehicles_us.csv') # leer los datos
st.header('Vehicles US')

disp_button = st.button('Construir Grafico de Dispersión')
if disp_button: 
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')            
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
