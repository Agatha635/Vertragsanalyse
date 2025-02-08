import streamlit as st

# ✅ WICHTIG: st.set_page_config MUSS direkt nach den Imports kommen!
st.set_page_config(
    page_title="Bauverträge smarter machen",
    page_icon="🏗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Jetzt erst das Logo anzeigen!
st.image("https://github.com/Agatha635/Vertragsanalyse/blob/main/logo.jpg?raw=true", width=200)

# ✅ Dark Mode & Design anpassen
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

# ✅ Titel und Einführungstext
st.title("Bauverträge smarter machen")
st.write("Willkommen zu deiner KI-gestützten Vertragsanalyse!")

# Hier kommt dein restlicher Code...
# Dein bestehender Code (Chat-Funktion, Upload etc.) kommt hier...
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
