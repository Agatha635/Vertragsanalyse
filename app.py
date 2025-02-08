import streamlit as st
import google.generativeai as genai

# 🔹 Streamlit-Seitenkonfiguration (muss als erstes kommen!)
st.set_page_config(
    page_title="Bauverträge smarter machen",
    page_icon="🏗",
    layout="wide"
)

# 🔹 Logo anzeigen (falls vorhanden)
st.image("https://github.com/Agatha635/Vertragsanalyse/blob/main/logo.jpg?raw=true", width=200)

# 🔹 Titel zentrieren & größer machen
st.markdown(
    """
    <h1 style='text-align: center; font-size: 50px; color: #008CBA;'>
        Bauverträge smarter machen
    </h1>
    """,
    unsafe_allow_html=True
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

# 🔹 Spalten-Layout für bessere Struktur
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Vertrag hochladen")
    uploaded_file = st.file_uploader("Lade einen Vertrag als Text hoch", type=["txt"])

with col2:
    st.subheader("📝 Manuelle Eingabe")
    contract_text = st.text_area("Hier den Vertragstext eingeben", height=200)

# 🔹 API-Schlüssel aus Streamlit-Secrets laden (SICHERHEIT!)
api_key = st.secrets["AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ"]
genai.configure(api_key=api_key)

# 🔹 KI-Analyse starten
if st.button("🔎 Vertrag analysieren"):
    if contract_text:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"""
        Analysiere den folgenden Bauvertrag gemäß den folgenden rechtlichen Grundlagen:
        - BGB (§§ 631 ff. Werkvertrag & Bauvertragsrecht §§ 650a ff.)
        - HOAI (Honorarordnung für Architekten und Ingenieure)
        - VOB/B (Vergabe- und Vertragsordnung für Bauleistungen, Teil B & C)
        - Bauordnungsrecht der Länder
        - BauFordSiG (Gesetz über die Sicherung der Bauforderungen)
        - MaBV (Makler- und Bauträgerverordnung)
        
        Identifiziere potenzielle Probleme, Verstöße oder unklare Regelungen und schlage konkrete Verbesserungen vor.
        
        Vertragstext:
        {contract_text}
        """
        response = model.generate_content(prompt)
        st.subheader("🔹 KI-Analyse & Verbesserungsvorschläge:")
        st.write(response.text)
    else:
        st.warning("⚠️ Bitte lade eine Datei hoch oder gib einen Vertrag ein!")
