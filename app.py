import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos de anuncios de venta de coches
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header('Dashboard de anuncios de venta de coches')

# Estado guardado: recuerda qué gráficas están visibles entre clics
if 'show_hist' not in st.session_state:
    st.session_state.show_hist = False
if 'show_scatter' not in st.session_state:
    st.session_state.show_scatter = False


def toggle_hist():
    # Prende o apaga la visibilidad del histograma
    st.session_state.show_hist = not st.session_state.show_hist


def toggle_scatter():
    # Prende o apaga la visibilidad del gráfico de dispersión
    st.session_state.show_scatter = not st.session_state.show_scatter


# Botón del histograma (cambia de texto según el estado)
hist_label = 'Ocultar histograma' if st.session_state.show_hist else 'Construir histograma'
st.button(hist_label, key='hist_button', on_click=toggle_hist)

if st.session_state.show_hist:
    st.write('Histograma del odómetro de los coches en venta')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, width='stretch')

# Botón del gráfico de dispersión (cambia de texto según el estado)
scatter_label = 'Ocultar gráfico de dispersión' if st.session_state.show_scatter else 'Construir gráfico de dispersión'
st.button(scatter_label, key='scatter_button', on_click=toggle_scatter)

if st.session_state.show_scatter:
    st.write('Relación entre el odómetro y el precio')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, width='stretch')