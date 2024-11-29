import streamlit as st
import plotly_express as px
import pandas as pd

st.header('Datos de anuncios de venta de coches')
car_data = pd.read_csv('vehicles_us.csv')
st.write('Selecciona histograma o gráfico de dispersión')
build_histogram = st.button('Crear un histograma')
build_scatter = st.button('Crear gráfico de dispersion')


if build_histogram:
    st.write('Histograma ventas de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
if build_scatter:
    st.write('Gráfico de dispersión de ventas de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)