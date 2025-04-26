import streamlit as st

# Configuración de la página
st.set_page_config(page_title="ViralGen AI", layout="centered")

st.title("🔥 ViralGen AI - Generador de Guiones Virales")

st.markdown("#### Completa el formulario para generar un guion viral que venda solo:")

# Formulario
with st.form("formulario_guion"):
    servicio = st.text_input("¿Qué servicio o producto quieres promocionar?")
    avatar = st.text_input("¿Quién es tu cliente ideal? (edad, profesión, situación, deseo principal)")
    dolor = st.text_input("¿Cuál es el principal problema o dolor que soluciona tu servicio?")
    resultado = st.text_input("¿Qué resultado espectacular promete tu servicio?")
    tono = st.selectbox("¿Qué tono quieres para el guion?", ["Agresivo", "Emocional", "Inspirador", "Polémico"])
    formula = st.selectbox("¿Qué fórmula de copywriting prefieres?", ["AIDA", "PAS", "4P", "Storytelling"])
    cta = st.text_input("¿Qué acción quieres que realice el usuario al final? (ej: agenda una llamada, compra ahora...)")
    
    enviado = st.form_submit_button("🔥 Generar Guion Viral")

# Procesamiento al enviar
if enviado:
    st.success("✅ ¡Guion generado con éxito!")

    st.markdown("---")
    st.subheader("📜 Guion Viral Generado:")

    guion = f"""
¡Atención! 🚨

¿Eres {avatar} y estás harto de {dolor}?

Con nuestro {servicio}, podrás {resultado} sin perder tiempo ni dinero.

No es solo una promesa: es un cambio real que ya ha transformado la vida de muchos como tú.

{{
    "tono": "{tono}",
    "fórmula": "{formula}"
}}

👉 {cta}
    """

    st.code(guion, language="markdown")
