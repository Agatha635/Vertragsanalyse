import streamlit as st

# 🌙 Dark Mode aktivieren & Primärfarbe ändern
st.set_page_config(
    page_title="Bauverträge smarter machen",
    page_icon="🏗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Farben für Buttons & Text anpassen
st.markdown(
    """
    <style>
        body {
            color: #ffffff;
            background-color: #1E1E1E;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stTextInput>div>div>input {
            background-color: #333333;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import google.generativeai as genai

# API-Schlüssel für Google Gemini KI
genai.configure(api_key="AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ")

st.title("🔍 KI-gestützte Vertragsanalyse")
st.write("Lade einen Bauvertrag hoch oder gib ihn manuell ein, um Verbesserungsvorschläge zu erhalten.")

# Datei-Upload
uploaded_file = st.file_uploader("Lade eine Textdatei hoch", type=["txt"])

# Falls Datei hochgeladen wird, lese den Inhalt
vertragstext = ""
if uploaded_file is not None:
    vertragstext = uploaded_file.read().decode("utf-8")
    st.text_area("📜 Vertragstext:", vertragstext, height=200)

# Alternativ: Manueller Texteingabe
else:
    vertragstext = st.text_area("Oder gib deinen Vertrag hier ein:", height=200)

# KI-Analyse starten
if st.button("🔎 Vertrag analysieren"):
    if vertragstext:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"Bitte überprüfe den folgenden Bauvertrag und schlage Verbesserungen vor:\n\n{vertragstext}"
        response = model.generate_content(prompt)
        st.subheader("🔹 KI-Analyse & Verbesserungsvorschläge:")
        st.write(response.text)
    else:
        st.warning("⚠️ Bitte lade eine Datei hoch oder gib einen Vertrag ein!")
