import streamlit as st
import random

st.set_page_config(
    page_title="Juego: Adivina el número",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 Juego: Adivina el número")

st.write(
    """
    Estoy pensando en un número secreto entre **1 y 100**.  
    Tienes **7 intentos** para adivinarlo.

    Después de cada intento te diré:
    - 👉 **El número por adivinar es mayor** 
    - 👉 **El número por adivinar es menor**
    """
)

# ----------------------------------------------------------
# Inicializar estado
# ----------------------------------------------------------
if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.intentos = 0
    st.session_state.juego_terminado = False
    st.session_state.ultimo_mensaje = ""

def nueva_partida():
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.intentos = 0
    st.session_state.juego_terminado = False
    st.session_state.ultimo_mensaje = ""

# ----------------------------------------------------------
# Botón de nueva partida (arriba) -> resetea y rerun
# ----------------------------------------------------------
if st.button("🔄 Nueva partida", type="secondary"):
    nueva_partida()
    st.success("Se ha iniciado una nueva partida. ¡Suerte! 🍀")
    st.rerun()  # aseguramos que todo se redibuje con el estado inicial

st.write("---")

# ----------------------------------------------------------
# FORMULARIO DEL INTENTO
# ----------------------------------------------------------
# Usamos un form para que el intento se procese solo cuando se hace submit
# ----------------------------------------------------------
with st.form("form_juego"):
    numero_usuario = st.number_input(
        "Escribe un número entre 1 y 100:",
        min_value=1,
        max_value=100,
        step=1,
        key="input_numero"
    )
    enviar = st.form_submit_button("Probar número")

# ----------------------------------------------------------
# LÓGICA DEL JUEGO
# ----------------------------------------------------------
if enviar and not st.session_state.juego_terminado:
    st.session_state.intentos += 1
    secreto = st.session_state.numero_secreto

    if numero_usuario == secreto:
        st.session_state.ultimo_mensaje = f"🎉 ¡Correcto! El número secreto era **{secreto}**."
        st.session_state.juego_terminado = True
    else:
        if numero_usuario > secreto:
            st.session_state.ultimo_mensaje = f"El número es menor 😅."
        else:
            st.session_state.ultimo_mensaje = f"El número es mayor 😅."

        if st.session_state.intentos >= 7:
            st.session_state.ultimo_mensaje += f" ❌ Se terminaron los intentos. El número era **{secreto}**."
            st.session_state.juego_terminado = True

# ----------------------------------------------------------
# MOSTRAR ESTADO ACTUAL (ya con el mensaje actualizado)
# ----------------------------------------------------------
st.write(f"Intentos usados: **{st.session_state.intentos} / 7**")
st.write(f"Intentos restantes: **{7 - st.session_state.intentos}**")

if st.session_state.ultimo_mensaje:
    st.info(st.session_state.ultimo_mensaje)

if st.session_state.juego_terminado:
    st.warning("El juego ha terminado. Si quieres, inicia una nueva partida arriba 👆")
