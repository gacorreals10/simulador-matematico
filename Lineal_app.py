# 📌 Importación de librerías necesarias
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🧾 Título de la app
st.title("Simulador de Funciones Lineales")

# 📚 Teoría básica
st.markdown("""
Una **función lineal** tiene la forma:

### f(x) = mx + b

Donde:
- **m** es la pendiente: indica si la recta sube, baja o es horizontal.
- **b** es la intersección con el eje Y.

Usa los sliders para modificar estos valores y observa el cambio en la gráfica.
""")

# 🎛️ Sliders interactivos
m = st.slider("📈 Pendiente (m)", -10.0, 10.0, 1.0, step=0.5)
b = st.slider("📍 Intersección con el eje Y (b)", -10.0, 10.0, 0.0, step=0.5)

# 🧮 Generar datos para la gráfica
x = np.linspace(-10, 10, 400)
y = m * x + b

# 📊 Dibujar la gráfica
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label=f"f(x) = {m}x + {b}")
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_title("Gráfica de la función lineal")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# 📘 Retroalimentación automática
st.markdown(f"""
### 🧠 Retroalimentación:
- Tu función actual es: **f(x) = {m}x + {b}**
- La pendiente es: **{m}**
- Corta el eje Y en: **(0, {b})**
""")

# ❓ Pregunta basada en la gráfica
st.markdown("## ❓ Pregunta de comprensión")

respuesta = st.radio(
    "Con la gráfica actual, ¿qué tipo de comportamiento tiene la recta?",
    (
        "A) Subida (creciente de izquierda a derecha)",
        "B) Bajada (decreciente de izquierda a derecha)",
        "C) Horizontal (no cambia)",
        "D) Es una curva"
    )
)

# ✔️ Evaluar la respuesta según el valor de la pendiente
if m > 0:
    correcta = "A"
elif m < 0:
    correcta = "B"
elif m == 0:
    correcta = "C"
else:
    correcta = None

if respuesta and correcta:
    if respuesta.startswith(correcta):
        st.success("✅ ¡Correcto! Has identificado bien el comportamiento de la recta.")
    else:
        st.error("❌ Esa no es la opción correcta. Observa bien la inclinación de la recta.")

# 🔁 Tip extra para el aprendizaje
st.info("""
🔎 **Consejo**:  
Recuerda que la pendiente (m) determina la inclinación:
- \( m > 0 \): la recta **sube**
- \( m < 0 \): la recta **baja**
- \( m = 0 \): la recta es **horizontal**
""")
