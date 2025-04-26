import streamlit as st

st.set_page_config(page_title="ViralGen AI - Generador de Guiones Virales", layout="centered")

st.title("🔥 ViralGen AI - Generador de Guiones Virales")
st.write("Completa el formulario para crear tu guión viral que impacte y venda solo:")

# Formulario
with st.form(key="formulario_guion"):
    producto = st.text_input("¿Qué servicio o producto quieres promocionar?")
    cliente_ideal = st.text_input("¿Quién es tu cliente ideal? (edad, profesión, situación, deseo principal)")
    problema = st.text_input("¿Cuál es el principal problema o dolor que soluciona tu servicio?")
    resultado = st.text_input("¿Qué resultado espectacular promete tu servicio?")
    tono = st.selectbox("¿Qué tono quieres para el guion?", ["Polémico", "Inspirador", "Agresivo", "Emocional"])
    formula = st.selectbox("¿Qué fórmula de copywriting prefieres?", ["AIDA", "PAS", "Antes-Después-Puente"])
    accion = st.text_input("¿Qué acción quieres que realice el usuario al final? (ej: agenda una llamada, compra ahora...)")
    enviar = st.form_submit_button("Generar Guión Viral 🚀")

# Lógica de generación
if enviar:
    st.success("✅ ¡Guion generado con éxito!")
    st.subheader("📜 Guion Viral Generado:")

    if formula == "AIDA":
        guion = f"""¡{tono.upper()} ALERTA! 🚨

¿Eres {cliente_ideal} y estás cansado de {problema}?

Imagina poder {resultado} gracias a {producto}.

Miles ya lo han conseguido... ¿Por qué tú no?

🔥 No te quedes fuera. ¡{accion.capitalize()} ahora!"""
    
    elif formula == "PAS":
        guion = f"""¿Te sientes como {cliente_ideal}, lidiando con {problema} todos los días?

Eso no tiene por qué seguir así.

Con {producto}, puedes lograr {resultado} mucho antes de lo que imaginas.

💥 {accion.capitalize()} y empieza el cambio hoy."""
    
    elif formula == "Antes-Después-Puente":
        guion = f"""ANTES: {cliente_ideal} atrapados en {problema}.

DESPUÉS: {resultado} de la mano de {producto}.

PUENTE: No es magia. Es estrategia. 🔥

👉 {accion.capitalize()} y da el salto que mereces."""

    else:
        guion = "⚠️ Fórmula no reconocida. Por favor, revisa tu selección."

    st.write(guion)
