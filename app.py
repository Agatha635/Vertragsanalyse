import streamlit as st

# Streamlit-Seitenkonfiguration
st.set_page_config(
    page_title="Bauverträge smarter machen",
    page_icon="🏗",
    layout="wide"
)

# Überschrift zentrieren & größer machen
st.markdown(
    "<h1 style='text-align: center; font-size: 50px; color: #008CBA;'>Bauverträge smarter machen</h1>",
    unsafe_allow_html=True
)
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🔹 Benutzerdefiniertes Styling mit CSS
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #005f73;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: black;
            border-radius: 5px;
            padding: 5px;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔹 Logo und Titel
st.image("https://github.com/Agatha635/Vertragsanalyse/blob/main/logo.jpg?raw=true", width=200)
st.markdown("<p class='title'>Bauverträge smarter machen</p>", unsafe_allow_html=True)

# 🔹 Spalten-Layout für bessere Struktur
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Vertrag hochladen")
    uploaded_file = st.file_uploader("Lade einen Vertrag als PDF oder Text hoch", type=["pdf", "txt"])

with col2:
    st.subheader("📝 Manuelle Eingabe")
    contract_text = st.text_area("Hier den Vertragstext eingeben", height=200)

# 🔹 KI-Analyse starten
if st.button("🚀 Vertrag analysieren"):
    st.success("✅ Analyse läuft... (Hier könnte deine KI-Antwort erscheinen)")


# Hier kommt dein restlicher Code...
# Dein bestehender Code (Chat-Funktion, Upload etc.) kommt hier...
import google.generativeai as genai

# API-Schlüssel für Google Gemini KI
genai.configure(api_key="AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ")


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
