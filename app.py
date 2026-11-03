import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Configuración de la página (debe ser el primer comando de Streamlit)
st.set_page_config(page_title='Dashboard de coches', page_icon='🚗')

# Leer los datos de anuncios de venta de coches
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado e introducción
st.header('🚗 Dashboard de anuncios de venta de coches')
st.write(
    'Explora de forma interactiva un conjunto de datos de coches usados en venta. '
    'Usa los botones para mostrar u ocultar cada gráfica y compararlas.'
)

# Métricas generales del conjunto de datos
col1, col2, col3 = st.columns(3)
col1.metric('Anuncios', f"{len(car_data):,}")
col2.metric('Precio mediano', f"${car_data['price'].median():,.0f}")
col3.metric('Odómetro mediano', f"{car_data['odometer'].median():,.0f}")

# Muestra de los datos, escondida en un desplegable
with st.expander('Ver una muestra de los datos'):
    st.dataframe(car_data.head(20))

st.divider()

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


# Botones lado a lado (el texto cambia según el estado)
hist_label = 'Ocultar histograma' if st.session_state.show_hist else 'Construir histograma'
scatter_label = (
    'Ocultar gráfico de dispersión' if st.session_state.show_scatter
    else 'Construir gráfico de dispersión'
)

btn_col1, btn_col2 = st.columns(2)
btn_col1.button(hist_label, key='hist_button', on_click=toggle_hist, width='stretch')
btn_col2.button(scatter_label, key='scatter_button', on_click=toggle_scatter, width='stretch')

# Histograma del odómetro
if st.session_state.show_hist:
    st.subheader('📊 Distribución del odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(xaxis_title='Odómetro', yaxis_title='Número de anuncios')
    st.plotly_chart(fig, width='stretch')
    st.caption(
        'La mayoría de los coches se concentra entre 50 mil y 150 mil de odómetro, '
        'y hay una cola larga con pocos coches de odómetro muy alto.'
    )

# Gráfico de dispersión odómetro vs. precio
if st.session_state.show_scatter:
    st.subheader('📈 Relación entre odómetro y precio')
    fig = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(opacity=0.4, size=5),
    )])
    fig.update_layout(xaxis_title='Odómetro', yaxis_title='Precio')
    st.plotly_chart(fig, width='stretch')
    st.caption(
        'A mayor odómetro, el precio tiende a bajar. '
        'Los puntos aislados son valores atípicos que valdría la pena revisar.'
    )