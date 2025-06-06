import streamlit as st

st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.15em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .szenario-box { background: #393e46; color: #fff; border-radius: 12px; padding: 1.1em 1.4em; margin: 1.3em 0 1.3em 0; border-left: 6px solid #00adb5; font-size: 1.05em; }
    .feedback-success { background: #eafff3; border-left: 6px solid #00c897; color: #222831; border-radius: 10px; padding: 1em 1.2em; margin-top: 1.2em; font-size: 1.08em; font-weight: 500; }
    .feedback-error { background: #fff2f2; border-left: 6px solid #ff6363; color: #222831; border-radius: 10px; padding: 1em 1.2em; margin-top: 1.2em; font-size: 1.08em; font-weight: 500; }
    
    .question-text {
        font-size: 1.1em;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 1em;
        line-height: 1.4;
    }
    
    /* Erzwinge dein aktuelles Theme auf allen Geräten */
    .stApp {
        background-color: #23272f !important;
        color: #ffffff !important;
    }
    
    /* Überschreibe System-Theme-Preferences */
    @media (prefers-color-scheme: light), (prefers-color-scheme: dark) {
        .stApp {
            background-color: #23272f !important;
            color: #ffffff !important;
        }
    }
    
    /* Mobile-spezifische Absicherung */
    @media only screen and (max-width: 768px) {
        .stApp {
            background-color: #23272f !important;
            color: #ffffff !important;
        }
    }
    
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Kapitel 4: Lernkontrolle</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Kundeninterview oder Datenanalyse?</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="szenario-box">'
    '<b>Szenario:</b> Du hast deine erste Version der nachhaltigen Ernährungs-App veröffentlicht. Nun möchtest du wissen, ob NutzerInnen wirklich das Rezept-Feed-Feature nutzen oder ob sie mehr Wert auf die CO₂-Daten legen.'
    '</div>',
    unsafe_allow_html=True
)

antworten = [
    "A: Du analysierst die App-Daten und siehst dir an, welche Rezepte am häufigsten angeklickt werden.",
    "B: Du führst ein Kundeninterview durch, um zu erfahren, welche Funktionen die NutzerInnen am meisten schätzen.",
    "C: Du startest direkt eine grosse Marketingkampagne, um das Feature weiter zu bewerben.",
    "D: Du fragst die NutzerInnen auf Social Media, ob sie das Feature nützlich finden."
]
feedback = [
    "Falsch. Datenanalyse ist hilfreich, aber sie sagt dir nicht genug über die Motivation der NutzerInnen. Ein Interview gibt dir tiefere Einsichten.",
    "Richtig! Kundeninterviews liefern tiefere, qualitative Einblicke und helfen dir, die wahren Bedürfnisse deiner Zielgruppe zu verstehen.",
    "Falsch. Eine Marketingkampagne vor der Validierung des Features könnte unnötige Ressourcen verschwenden.",
    "Falsch. Social Media kann eine schnelle Reaktion bieten, aber es ist nicht die beste Methode, um fundierte Entscheidungen zu treffen."
]
richtige_antwort = 1  # Index für Antwort B

if "ld1_radio_key" not in st.session_state:
    st.session_state["ld1_radio_key"] = 0
if "ld1_abgegeben" not in st.session_state:
    st.session_state["ld1_abgegeben"] = False
if "ld1_feedback" not in st.session_state:
    st.session_state["ld1_feedback"] = None

# Große, fette Frage als HTML
st.markdown(
    '<div class="question-text">'
    'Wie gehst du jetzt vor, um zu verstehen, welche Features für deine NutzerInnen wichtig sind?'
    '</div>',
    unsafe_allow_html=True
)

# Radio-Button mit kleinerem Label
auswahl = st.radio(
    "Antwort auswählen:",
    antworten,
    key=f"ld1_radio_{st.session_state['ld1_radio_key']}",
    disabled=st.session_state["ld1_abgegeben"]
)

if not st.session_state["ld1_abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["ld1_abgegeben"] = True
        if antworten.index(auswahl) == richtige_antwort:
            st.session_state["ld1_feedback"] = "richtig"
        else:
            st.session_state["ld1_feedback"] = "falsch"
        st.rerun()

if st.session_state["ld1_abgegeben"]:
    idx = antworten.index(auswahl)
    if st.session_state["ld1_feedback"] == "richtig":
        st.markdown(f'<div class="feedback-success">{feedback[idx]}</div>', unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("Weiter"):
            st.session_state["ld1_abgegeben"] = False
            st.session_state["ld1_radio_key"] += 1
            st.switch_page("pages/10_Kapitel 4_Teil 2.py")
    else:
        st.markdown(f'<div class="feedback-error">{feedback[idx]}</div>', unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("Wiederholen"):
            st.session_state["ld1_abgegeben"] = False
            st.session_state["ld1_radio_key"] += 1
            st.rerun()
