"""
Mini dashboard con Streamlit para el dataset de diabetes.

Este script está pensado como TUTORIAL para principiantes:
- Muestra cómo crear una app muy sencilla con Streamlit.
- Utiliza un dataframe de ejemplo: diabetes_dataset.csv
- Agrega filtros básicos y algunas gráficas.

Pasos para usarlo:
1) Instala streamlit:  pip install streamlit
2) Guarda este archivo como: 21_Streamlit.py
3) Coloca diabetes_dataset.csv en la misma carpeta.
4) En la terminal, ejecuta: python -m streamlit run 21_Streamlit.py
"""

# ==========================================================
# 1. IMPORTAR LIBRERÍAS
# ==========================================================
# streamlit: para crear la interfaz web
# pandas: para manejar dataframes
# numpy: opcional para algunos cálculos numéricos
# matplotlib: para hacer gráficas y mostrarlas en streamlit
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# 2. CONFIGURACIÓN BÁSICA DE LA PÁGINA
# ==========================================================
# Esta función permite configurar título de la pestaña, layout, etc.
# ==========================================================
st.set_page_config(
    page_title="Mini Dashboard Diabetes",
    page_icon="🩺",
    layout="wide",  # "centered" o "wide"
)


# ==========================================================
# 3. FUNCIÓN PARA CARGAR LOS DATOS
# ==========================================================
# Usamos @st.cache_data para que la carga se "memorice"
# y no se vuelva a leer el CSV cada vez que el usuario interactúa.
# ==========================================================
@st.cache_data
def load_data():
    # Importante: diabetes_dataset.csv debe estar en la misma carpeta.
    df = pd.read_csv("diabetes_dataset.csv")
    return df


# Llamamos a la función de carga
df = load_data()


# ==========================================================
# 4. TÍTULO PRINCIPAL Y DESCRIPCIÓN
# ==========================================================
# st.title, st.subheader, st.write sirven para mostrar texto en la app.
# ==========================================================
st.title("🩺 Mini Dashboard – Diabetes Dataset")
st.write(
    """
    Esta interfaz es un *ejemplo básico con Streamlit* para visualizar el dataset de diabetes.
    
    Puedes:
    - Explorar la tabla de datos.
    - Filtrar por género, edad y estado de diabetes.
    - Ver algunos indicadores rápidos.
    - Ver gráficas simples (histograma, dispersión).
    
    La idea es que puedas adaptar este código para tus propios proyectos. 🙂
    """
)


# ==========================================================
# 5. SIDEBAR (BARRA LATERAL) PARA CONTROLES
# ==========================================================
# Todo lo que pongamos dentro de st.sidebar aparecerá a la izquierda.
# Aquí pondremos los filtros que el usuario puede mover.
# ==========================================================

st.sidebar.header("⚙️ Controles")

# 5.1. Selección de número de filas a mostrar
n_rows = st.sidebar.slider(
    "Número de filas a mostrar en la tabla",
    min_value=5,
    max_value=100,
    value=20,
    step=1,
)

# 5.2. Filtro por género
# Obtenemos los valores únicos de la columna 'gender' para armar el multiselect.
gender_options = df["gender"].unique().tolist()

# df["gender"]
# df.gender
# df.loc[:,"gender"]
# df.iloc[:,1]

gender_filter = st.sidebar.multiselect(
    "Filtrar por género",
    options=gender_options,
    default=gender_options,  # por default, todos seleccionados
)

# 5.3. Filtro por rango de edad
min_age = float(df["age"].min())
max_age = float(df["age"].max())

age_range = st.sidebar.slider(
    "Rango de edad",
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age),
    step= 1.0
)

# 5.4. Filtro: sólo pacientes con diabetes (checkbox)
only_diabetes = st.sidebar.checkbox(
    "Mostrar sólo pacientes con diabetes",
    value=False
)

# 5.5. Botón opcional para mostrar/ocultar descripción de los datos
show_description = st.sidebar.checkbox(
    "Mostrar descripción (describe)",
    value=False
)


# ==========================================================
# 6. APLICAR FILTROS AL DATAFRAME
# ==========================================================
# Partimos del dataframe original y vamos filtrando paso a paso.
# ==========================================================

df_filtered = df.copy()

# Filtro por género
if gender_filter:
    df_filtered = df_filtered[df_filtered["gender"].isin(gender_filter)]

# Filtro por rango de edad
df_filtered = df_filtered[
    (df_filtered["age"] >= age_range[0]) &
    (df_filtered["age"] <= age_range[1])
]

# Filtro por diabetes (si el checkbox está activado)
if only_diabetes:
    df_filtered = df_filtered[df_filtered["diabetes"] == 1]


# ==========================================================
# 7. MOSTRAR TABLA DE DATOS
# ==========================================================
# Mostramos la tabla filtrada, recortada al número de filas que eligió el usuario.
# ==========================================================

st.subheader("📋 Datos filtrados")

st.write(
    f"Mostrando **{min(n_rows, len(df_filtered))} filas** "
    f"de un total de **{len(df_filtered)} filas filtradas**."
)

st.dataframe(df_filtered.head(n_rows))

# Si el usuario quiere ver la descripción (describe)
if show_description:
    st.subheader("📊 Descripción estadística (describe)")
    st.write(df_filtered.describe())


# ==========================================================
# 8. MÉTRICAS RÁPIDAS (KPIs)
# ==========================================================
# Usamos st.columns para organizar las métricas en columnas.
# ==========================================================

st.subheader("📌 Métricas rápidas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total de pacientes (filtrados)",
        value=len(df_filtered),
    )

with col2:
    # Proporción de pacientes con diabetes en el subconjunto filtrado
    if len(df_filtered) > 0:
        diabetes_rate = df_filtered["diabetes"].mean()
    else:
        diabetes_rate = 0.0
    st.metric(
        label="Tasa de diabetes (filtrada)",
        value=f"{diabetes_rate:.2%}",
    )

with col3:
    # Edad promedio en el subconjunto filtrado
    if len(df_filtered) > 0:
        avg_age = df_filtered["age"].mean()
    else:
        avg_age = np.nan
    st.metric(
        label="Edad promedio (filtrada)",
        value=f"{avg_age:.1f}" if not np.isnan(avg_age) else "N/A",
    )


# ==========================================================
# 9. GRÁFICA 1 – HISTOGRAMA DE EDAD
# ==========================================================
# Usamos matplotlib para graficar, y luego st.pyplot para mostrar en streamlit.
# ==========================================================

st.subheader("📈 Histograma de edad (datos filtrados)")

# Sólo graficar si hay datos
if len(df_filtered) > 0:
    fig1, ax1 = plt.subplots()
    ax1.hist(df_filtered["age"], bins=20)
    ax1.set_title("Histograma de edad")
    ax1.set_xlabel("Edad")
    ax1.set_ylabel("Frecuencia")
    st.pyplot(fig1)
else:
    st.write("No hay datos para mostrar el histograma (revisa tus filtros).")


# ==========================================================
# 10. GRÁFICA 2 – BARRAS: DISTRIBUCIÓN DE DIABETES
# ==========================================================
# Construimos una pequeña tabla con la proporción de diabetes 0 y 1.
# ==========================================================

st.subheader("📊 Distribución de diabetes (0 = no, 1 = sí)")

if len(df_filtered) > 0:
    diabetes_counts = df_filtered["diabetes"].value_counts().sort_index()
    # Streamlit tiene un bar_chart que recibe un DataFrame o Serie
    st.bar_chart(diabetes_counts)
else:
    st.write("No hay datos para mostrar la distribución (revisa tus filtros).")


# ==========================================================
# 11. GRÁFICA 3 – DISPERSIÓN EDAD VS NIVEL DE GLUCOSA
# ==========================================================
# Scatter plot de 'age' vs 'blood_glucose_level', coloreando por diabetes.
# ==========================================================

st.subheader("🧪 Dispersión: Edad vs nivel de glucosa")

if len(df_filtered) > 0:
    # Preparamos los datos
    x = df_filtered["age"].to_numpy()
    y = df_filtered["blood_glucose_level"].to_numpy()
    d = df_filtered["diabetes"].to_numpy()

    # Creamos un arreglo de colores (rojo si diabetes = 1, azul si diabetes = 0)
    colores = np.where(d == 1, "red", "blue")

    fig2, ax2 = plt.subplots()
    scatter = ax2.scatter(x, y, c=colores, alpha=0.5)

    ax2.set_title("Edad vs nivel de glucosa (color = diabetes)")
    ax2.set_xlabel("Edad")
    ax2.set_ylabel("blood_glucose_level")

    # Leyenda simple usando handles manuales
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Sin diabetes (0)',
               markerfacecolor='blue', markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Con diabetes (1)',
               markerfacecolor='red', markersize=8),
    ]
    ax2.legend(handles=legend_elements, loc="best")

    st.pyplot(fig2)
else:
    st.write("No hay datos para mostrar la dispersión (revisa tus filtros).")


# ==========================================================
# 12. NOTA FINAL
# ==========================================================
# A partir de aquí, los alumnos pueden:
# - Agregar más filtros en el sidebar.
# - Crear más métricas.
# - Agregar nuevas gráficas (boxplots, violin plots, mapas de calor, etc.).
# - Integrar sus propios modelos de machine learning y mostrar resultados.
# ==========================================================
st.info(
    """
    ✅ **Tip para tus proyectos**:
    Puedes tomar esta app como base y:
    - Cambiar el dataset.
    - Agregar tus propias columnas calculadas (features).
    - Mostrar resultados de un modelo de clasificación o regresión.
    - Crear páginas adicionales usando `st.sidebar.radio` o `st.tabs`.
    """
)