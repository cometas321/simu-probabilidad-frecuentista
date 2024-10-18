import streamlit as st
import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt

# Función para cargar imágenes
def cargar_imagen(ruta):
    return Image.open(ruta)

# Título de la aplicación
st.title("Simulación de Lanzamiento de una Moneda o Dado")

# Introducción
st.write("""
Esta es una simulación del lanzamiento de una moneda o dado. 
Puedes elegir cuántos lanzamientos realizar, y la aplicación te mostrará cómo 
la frecuencia relativa cambia a medida que se realizan más lanzamientos.
""")

# Selección del tipo de simulación (Moneda o Dado)
opcion = st.selectbox("Elige entre lanzar una moneda o un dado:", ["Moneda", "Dado"])

# Entrada del usuario: número de lanzamientos
n_lanzamientos = st.slider("Selecciona el número de lanzamientos:", min_value=10, max_value=10000, value=100)

# Simulación de lanzamientos
if opcion == "Moneda":
    resultados = np.random.choice([0, 1], size=n_lanzamientos)  # 0: Cruz, 1: Cara
    frecuencia = np.cumsum(resultados) / np.arange(1, n_lanzamientos + 1)
else:
    resultados = np.random.choice([1, 2, 3, 4, 5, 6], size=n_lanzamientos)
    frecuencia = np.cumsum(resultados == 6) / np.arange(1, n_lanzamientos + 1)  # Frecuencia relativa del número 6

# Mostrar el gráfico de resultados
st.subheader(f"Resultados de {n_lanzamientos} lanzamientos")

fig, ax = plt.subplots()
ax.plot(frecuencia, label='Frecuencia relativa', color='blue')
if opcion == "Moneda":
    ax.axhline(y=0.5, color='red', linestyle='--', label='Probabilidad Teórica (0.5)')
    ax.set_title('Frecuencia Relativa de "Cara" en Lanzamientos de Moneda')
else:
    ax.axhline(y=1/6, color='red', linestyle='--', label='Probabilidad Teórica (1/6)')
    ax.set_title('Frecuencia Relativa de "6" en Lanzamientos de Dado')
    
ax.set_xlabel('Número de lanzamientos')
ax.set_ylabel('Frecuencia relativa')
ax.legend()
ax.grid(True)

# Mostrar la gráfica en la aplicación Streamlit
st.pyplot(fig)

# Mostrar los resultados finales
st.write(f"Después de {n_lanzamientos} lanzamientos:")
if opcion == "Moneda":
    st.write(f"- La frecuencia relativa de 'cara' es {frecuencia[-1]:.4f}.")
else:
    st.write(f"- La frecuencia relativa de '6' es {frecuencia[-1]:.4f}.")

