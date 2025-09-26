import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Visualización de Datos Simulados')

st.write("""
Esta aplicación genera datos aleatorios y muestra un histograma y un diagrama de dispersión.
""")

# Generar datos simulados
np.random.seed(42)
n_samples = st.slider('Número de muestras', 100, 1000, 500)
data = pd.DataFrame({
    'Columna A': np.random.randn(n_samples),
    'Columna B': np.random.rand(n_samples) * 100,
    'Columna C': np.random.randint(0, 10, n_samples)
})

st.subheader('Datos Simulados (Primeras 5 filas)')
st.write(data.head())

# Histograma
st.subheader('Histograma de Columna A')
fig, ax = plt.subplots()
ax.hist(data['Columna A'], bins=20)
st.pyplot(fig)

# Diagrama de Dispersión
st.subheader('Diagrama de Dispersión (Columna A vs Columna B)')
fig, ax = plt.subplots()
ax.scatter(data['Columna A'], data['Columna B'])
st.pyplot(fig)

st.subheader('Diagrama de Dispersión (Columna B vs Columna C)')
fig, ax = plt.subplots()
ax.scatter(data['Columna B'], data['Columna C'])
st.pyplot(fig)
