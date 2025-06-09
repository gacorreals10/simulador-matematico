import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🧱 Título del simulador
st.title("Simulador Interactivo de Funciones Cuadráticas")

# 📝 Introducción teórica breve
st.markdown("""
Una función cuadrática tiene la forma:  
\\( f(x) = ax^2 + bx + c \\)

Modifica los valores de **a**, **b** y **c** para observar cómo cambia la gráfica de la parábola.
""")

# 🎚️ Sliders para valores a, b y c
a = st.slider("Coeficiente a", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
b = st.slider("Coeficiente b", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
c = st.slider("Coeficiente c", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# 📈 Generar la gráfica
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

fig, ax = plt.subplots()
ax.plot(x, y, label=f'f(x) = {a:.1f}x² + {b:.1f}x + {c:.1f}')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True)
ax.legend()
st.pyplot(fig)

# 💡 Explicación de lo que ocurre con la gráfica
st.subheader("📘 Observaciones")
if a > 0:
    st.markdown("- La parábola **abre hacia arriba**.")
elif a < 0:
    st.markdown("- La parábola **abre hacia abajo**.")
else:
    st.markdown("- No es una parábola (es una línea recta).")

st.markdown(f"- El vértice está en: \\( x = {-b/(2*a):.2f} \\)")

# 🧠 Ejercicio práctico
st.subheader("🎯 Ejercicio para el estudiante")

st.markdown("""
Dada la siguiente parábola:

> \\( f(x) = -2x^2 + 4x + 6 \\)

**1. ¿Dónde se encuentra el vértice?**  
**2. ¿La parábola abre hacia arriba o hacia abajo?**  
**3. ¿Cuáles son las raíces (si existen)?**

👉 Calcula mentalmente o con papel, y luego responde:
""")

# ✅ Preguntas tipo test
st.subheader("📝 Preguntas de selección múltiple")

preg1 = st.radio("1. ¿Dónde se encuentra el vértice de la parábola?", [
    "En x = -1", 
    "En x = 1", 
    "En x = 2", 
    "En x = 0"
])

preg2 = st.radio("2. ¿La parábola abre hacia arriba o hacia abajo?", [
    "Hacia arriba", 
    "Hacia abajo", 
    "Es horizontal", 
    "No tiene forma de parábola"
])

preg3 = st.radio("3. ¿Cuántas raíces tiene esta parábola?", [
    "Una raíz", 
    "Dos raíces reales", 
    "Ninguna raíz real", 
    "Infinitas raíces"
])

# 🔍 Retroalimentación
st.subheader("🔍 Retroalimentación")

if st.button("Verificar respuestas"):
    if preg1 == "En x = 1":
        st.success("✔️ Correcto. El vértice está en x = -b/2a = -4/-4 = 1.")
    else:
        st.error("❌ Incorrecto. El vértice está en x = 1.")

    if preg2 == "Hacia abajo":
        st.success("✔️ Correcto. El coeficiente 'a' es -2, así que la parábola abre hacia abajo.")
    else:
        st.error("❌ Incorrecto. 'a' es negativo, por lo tanto la parábola abre hacia abajo.")

    if preg3 == "Dos raíces reales":
        st.success("✔️ Correcto. El discriminante (b² - 4ac) = 16 + 48 = 64, que es positivo.")
    else:
        st.error("❌ Incorrecto. Esta parábola tiene dos raíces reales.")

# 📌 Nota final
st.markdown("---")
st.info("Este simulador forma parte de un software educativo para el aprendizaje visual e interactivo de funciones cuadráticas.")
