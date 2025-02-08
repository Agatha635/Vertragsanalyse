import streamlit as st
import google.generativeai as genai
import pdfplumber  # 📄 Zum Extrahieren von Text aus PDFs

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
    </style>
    """,
    unsafe_allow_html=True
)

# 🔹 Spalten-Layout für bessere Struktur
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Vertrag hochladen")
    uploaded_file = st.file_uploader("Lade einen Vertrag als PDF oder Text hoch", type=["pdf", "txt"])

with col2:
    st.subheader("📝 Manuelle Eingabe")
    contract_text = st.text_area("Hier den Vertragstext eingeben", height=200)

# 🔹 API-Schlüssel direkt im Code setzen (nur für Tests!)
genai.configure(api_key="AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ")  # Ersetze "DEIN_API_KEY_HIER" mit deinem echten API-Schlüssel

# 🔹 Funktion zum Extrahieren von Text aus PDFs
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# 🔹 KI-Analyse starten
if st.button("🔎 Vertrag analysieren"):
    if uploaded_file:  # Falls eine Datei hochgeladen wurde
        if uploaded_file.type == "application/pdf":
            contract_text = extract_text_from_pdf(uploaded_file)
        else:
            contract_text = uploaded_file.read().decode("utf-8")

    if contract_text:  # Falls ein Vertragstext vorhanden ist
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"Bitte überprüfe den folgenden Bauvertrag und schlage Verbesserungen vor:\n\n{contract_text}"
        response = model.generate_content(prompt)
        st.subheader("🔹 KI-Analyse & Verbesserungsvorschläge:")
        st.write(response.text)
    else:
        st.warning("⚠️ Bitte lade eine Datei hoch oder gib einen Vertrag ein!")
