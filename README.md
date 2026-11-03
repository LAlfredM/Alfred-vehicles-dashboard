# Alfred-vehicles-dashboard

Dashboard web interactivo para explorar un conjunto de datos de anuncios de venta de coches, hecho con **Streamlit** y **Plotly**.

## ¿Qué hace la app?

- Muestra un histograma de la distribución del odómetro de los coches.
- Muestra un gráfico de dispersión de la relación entre odómetro y precio.
- Cada gráfica se construye al hacer clic en su botón y permanece visible; al volver a hacer clic, se oculta.
- Las dos gráficas pueden verse al mismo tiempo para compararlas.

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