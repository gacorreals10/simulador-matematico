import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador: Sistemas de Ecuaciones", layout="centered")

st.title("🧮 Simulador de Sistemas de Ecuaciones Lineales")
st.write("Modifica los coeficientes del sistema para observar cómo cambian las rectas en el plano cartesiano.")

# Entrada de coeficientes para las ecuaciones
st.subheader("🔧 Ajusta los valores de las ecuaciones:")
a1 = st.slider("Coeficiente a₁", -10, 10, 1)
b1 = st.slider("Coeficiente b₁", -10, 10, -1)
c1 = st.slider("Constante c₁", -20, 20, 2)

a2 = st.slider("Coeficiente a₂", -10, 10, 2)
b2 = st.slider("Coeficiente b₂", -10, 10, 1)
c2 = st.slider("Constante c₂", -20, 20, 4)

# Representación gráfica
x = np.linspace(-10, 10, 400)
try:
    y1 = (c1 - a1*x)/b1
    y2 = (c2 - a2*x)/b2

    fig, ax = plt.subplots()
    ax.plot(x, y1, label="Ecuación 1", color="blue")
    ax.plot(x, y2, label="Ecuación 2", color="green")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.info("Las rectas pueden cortarse en un punto (una solución), coincidir (infinitas soluciones) o no tocarse (ninguna solución).")

except ZeroDivisionError:
    st.error("⚠️ Error: No se puede dividir por cero. Ajusta los valores de b₁ y b₂.")

# -----------------------------------------------------------
# ✅ EJERCICIO 1 RELACIONADO CON LA SIMULACIÓN
# -----------------------------------------------------------
st.subheader("📘 Ejercicio de comprensión sobre el gráfico generado:")

st.write("Observa la gráfica generada y responde:")
ejercicio = st.radio(
    "¿Qué tipo de solución representa el sistema de ecuaciones mostrado?",
    (
        "Una única solución (las rectas se cruzan en un solo punto)",
        "Infinitas soluciones (las rectas coinciden completamente)",
        "Ninguna solución (las rectas son paralelas)",
        "No se puede saber con solo ver la gráfica"
    )
)

# Cálculo de determinante para dar la respuesta correcta
det = a1 * b2 - a2 * b1

if ejercicio:
    if det != 0:
        correcta = "Una única solución (las rectas se cruzan en un solo punto)"
    elif a1 * b2 == a2 * b1 and a1 * c2 == a2 * c1:
        correcta = "Infinitas soluciones (las rectas coinciden completamente)"
    else:
        correcta = "Ninguna solución (las rectas son paralelas)"

    if ejercicio == correcta:
        st.success("✅ ¡Correcto! Has identificado correctamente el tipo de sistema.")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta es: **{correcta}**. Observa la inclinación y posición de las rectas para determinarlo.")
