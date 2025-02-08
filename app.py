import streamlit as st
import google.generativeai as genai

# 🔹 Streamlit-Seitenkonfiguration
st.set_page_config(
    page_title="Bauverträge smarter machen",
    page_icon="🏗",
    layout="wide"
)

# 🔹 Titel & Design
st.markdown(
    """
    <h1 style='text-align: center; font-size: 50px; color: #008CBA;'>
        Bauverträge smarter machen
    </h1>
    """,
    unsafe_allow_html=True
)

# 🔹 Datei-Upload oder manuelle Texteingabe
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Vertrag hochladen")
    uploaded_file = st.file_uploader("Lade einen Vertrag als Text hoch", type=["txt"])

with col2:
    st.subheader("📝 Manuelle Eingabe")
    contract_text = st.text_area("Hier den Vertragstext eingeben", height=200)

# 🔹 API-Schlüssel direkt im Code setzen (Nur für lokale Tests!)
API_KEY = "AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ"
genai.configure(api_key=API_KEY)

# 🔹 KI-Analyse starten
if st.button("🔎 Vertrag analysieren"):
    if contract_text:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"""Analysiere den folgenden Bauvertrag nach folgenden Rechtsgrundlagen:
        - BGB-Bauvertragsrecht
        - HOAI (Honorarordnung für Architekten und Ingenieure)
        - VOB (Vergabe- und Vertragsordnung für Bauleistungen)
        - Bauordnungsrecht der Länder
        - BauFordSiG (BauFordSiG)
        - MaBV (Makler- und Bauträgerverordnung)
        
        Bitte identifiziere mögliche Probleme und gib konkrete Verbesserungsvorschläge mit Paragraphenangaben:
        {contract_text}"""

        response = model.generate_content(prompt)
        st.subheader("🔹 KI-Analyse & Verbesserungsvorschläge:")
        st.write(response.text)
    else:
        st.warning("⚠️ Bitte lade eine Datei hoch oder gib einen Vertrag ein!")


