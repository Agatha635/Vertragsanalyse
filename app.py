import streamlit as st
import google.generativeai as genai

# Streamlit-Seitenkonfiguration
st.set_page_config(
    page_title="Bauverträge smarter machen",
    page_icon="🏗",
    layout="wide"
)

# Logo anzeigen
st.image("https://github.com/Agatha635/Vertragsanalyse/blob/main/logo.jpg?raw=true", width=200)

# Titel
st.markdown(
    "<h1 style='text-align: center; font-size: 50px; color: #008CBA;'>Bauverträge smarter machen</h1>",
    unsafe_allow_html=True
)

# Spalten-Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Vertrag hochladen")
    uploaded_file = st.file_uploader("Lade einen Vertrag als TXT hoch", type=["txt"])

    # Text aus Datei auslesen
    if uploaded_file is not None:
        contract_text = uploaded_file.getvalue().decode("utf-8")
    else:
        contract_text = ""

with col2:
    st.subheader("📝 Manuelle Eingabe")
    manual_text = st.text_area("Hier den Vertragstext eingeben", height=200)

    # Falls Nutzer Text eingibt, überschreibt das den Datei-Text
    if manual_text:
        contract_text = manual_text

# API-Schlüssel (lokale Nutzung)
api_key = "AIzaSyAreBEXHIDbUvjS7RWoqIVGgAETBcoWBKQ"  # Ersetze mit deinem echten API-Schlüssel
genai.configure(api_key=api_key)

# Auswahl der Analyse-Tiefe
analyse_tiefe = st.radio(
    "🔍 Wähle die Tiefe der Vertragsanalyse:",
    ("Basis-Analyse", "Erweiterte Analyse", "Detaillierte Analyse")
)

# Dynamischer Prompt je nach Auswahl
if analyse_tiefe == "Basis-Analyse":
    prompt = f"Analysiere diesen Bauvertrag allgemein: \n\n{contract_text}"

elif analyse_tiefe == "Erweiterte Analyse":
    prompt = f"""
    Analysiere den folgenden Bauvertrag nach diesen Rechtsgrundlagen:

    - BGB-Bauvertragsrecht
    - HOAI
    - VOB
    - Bauordnungsrecht der Länder
    - BauFordSiG
    - MaBV

    Vertragstext:
    {contract_text}
    """

elif analyse_tiefe == "Detaillierte Analyse":
    prompt = f"""
    Erstelle eine tiefgehende Analyse mit Paragrafenangaben:

    - BGB-Bauvertragsrecht (§§ 631 ff. BGB)
    - HOAI (§§ 1-16 HOAI)
    - VOB (VOB/B, VOB/C)
    - Bauordnungsrecht (je nach Bundesland)
    - BauFordSiG (§ 1 BauFordSiG)
    - MaBV (§§ 1-16 MaBV)

    Vertragstext:
    {contract_text}
    """

# KI-Analyse starten
if st.button("🔎 Vertrag analysieren"):
    if contract_text.strip():  # Prüft, ob Text vorhanden ist
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        st.subheader("🔹 KI-Analyse & Verbesserungsvorschläge:")
        st.write(response.text)
    else:
        st.warning("⚠️ Bitte lade eine Datei hoch oder gib einen Vertrag ein!")
