# Alfred-vehicles-dashboard

Dashboard web interactivo para explorar un conjunto de datos de anuncios de venta de coches, hecho con **Streamlit** y **Plotly**.

## ¿Qué hace la app?

- Muestra métricas generales del conjunto de datos: número de anuncios, precio mediano y odómetro mediano.
- Permite ver una muestra de los datos en un desplegable.
- Construye un histograma de la distribución del odómetro de los coches.
- Construye un gráfico de dispersión de la relación entre odómetro y precio.
- Cada gráfica se construye al hacer clic en su botón y permanece visible hasta que se oculta con otro clic, así que ambas pueden compararse al mismo tiempo.

## Archivos del proyecto

- `app.py`: código de la aplicación web.
- `vehicles_us.csv`: datos utilizados.
- `notebooks/EDA.ipynb`: análisis exploratorio de datos.
- `requirements.txt`: librerías necesarias.

## Cómo correrlo localmente

```
pip install -r requirements.txt
streamlit run app.py
```

## App desplegada

🔗 Link a la app en Render: https://alfred-vehicles-dashboard.onrender.com
> Nota: la app está en el plan gratuito de Render y se "duerme" tras un rato sin uso; la primera carga puede tardar hasta un minuto.