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

# 🔹 Spalten-Layout für bessere Struktur
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Vertrag hochladen")
    uploaded_file = st.file_uploader("Lade einen Vertrag als PDF oder Text hoch", type=["pdf", "txt"])

with col2:
    st.subheader("📝 Manuelle Eingabe")
    contract_text = st.text_area("Hier den Vertragstext eingeben", height=200)

# 🔹 API-Schlüssel für die KI (lokal direkt setzen, nicht über st.secrets)
api_key = "AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ"  # Ersetze durch deinen echten API-Schlüssel
genai.configure(api_key=api_key)

# 🔹 Auswahl der Analyse-Tiefe
analyse_tiefe = st.radio(
    "🔍 Wähle die Tiefe der Vertragsanalyse:",
    ("Basis-Analyse", "Erweiterte Analyse", "Detaillierte Analyse")
)

# 🔹 Dynamischer Prompt je nach Auswahl
if analyse_tiefe == "Basis-Analyse":
    prompt = f"Analysiere den Vertrag allgemein auf Verständlichkeit, Vollständigkeit und eventuelle Unklarheiten."

elif analyse_tiefe == "Erweiterte Analyse":
    prompt = f"""
    Analysiere den Vertrag basierend auf folgenden Rechtsgrundlagen:
    - BGB-Bauvertragsrecht
    - HOAI (Honorarordnung für Architekten und Ingenieure)
    - VOB (Vergabe- und Vertragsordnung für Bauleistungen)
    - Bauordnungsrecht der Länder
    - BauFordSiG (Bauforderungssicherungsgesetz)
    - MaBV (Makler- und Bauträgerverordnung)
    """

elif analyse_tiefe == "Detaillierte Analyse":
    prompt = f"""
    Erstelle eine tiefgehend
