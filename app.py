import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Gráfica de histograma y diagrama de dispersión')
# hist_button = st.button('Construir histograma')  # crear un botón
build_histogram = st.checkbox('Construir un histograma')

# if hist_button:  # al hacer clic en el botón
if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

# hist_button2 = st.button('Construir dispersión')  # crear un botón
build_histogram2 = st.checkbox('Construir un diagrama de dispersión')

if build_histogram2:
    # hist_button2:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
