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

    if uploaded_file is not None:
        contract_text = uploaded_file.read().decode("utf-8")  # 🟢 Text aus Datei lesen
    else:
        contract_text = ""

with col2:
    st.subheader("📝 Manuelle Eingabe")
    manual_text = st.text_area("Hier den Vertragstext eingeben", height=200)

# Falls manuelle Eingabe vorhanden, diese priorisieren
if manual_text:
    contract_text = manual_text

# 🔹 API-Schlüssel direkt im Code setzen (Nur für lokale Tests!)
API_KEY = "AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ"
genai.configure(api_key=API_KEY)

# 🔹 KI-Analyse starten
if st.button("🔎 Vertrag analysieren"):
    if contract_text.strip():  # 🟢 Prüfen, ob Text vorhanden ist
        model = genai.GenerativeModel("gemini-pro")
        prompt = (
            "Analysiere den folgenden Bauvertrag nach folgenden Rechtsgrundlagen:\n"
            "- BGB-Bauvertragsrecht\n"
            "- HOAI (Honorarordnung für Architekten und Ingenieure)\n"
            "- VOB (Vergabe- und Vertrag
