import streamlit as st

st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.15em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .feedback-success { background: #eafff3; border-left: 6px solid #00c897; color: #222831; border-radius: 10px; padding: 1em 1.2em; margin-top: 1.2em; font-size: 1.08em; font-weight: 500; }
    .feedback-error { background: #fff2f2; border-left: 6px solid #ff6363; color: #222831; border-radius: 10px; padding: 1em 1.2em; margin-top: 1.2em; font-size: 1.08em; font-weight: 500; }

    .question-text {
        font-size: 1.1em;
        color: #ffffff;
        margin-bottom: 1em;
        line-height: 1.4;
    }  /* SCHLIESSENDE KLAMMER HINZUGEFÜGT */
    
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
st.markdown('<div class="subtitle">Ressourcen sinnvoll einsetzen</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# Große, fette Frage als HTML
st.markdown(
    '<div class="question-text">'
    'Du hast ein einfaches MVP entwickelt, das ein grundlegendes Rezept-Feed bietet, aber die NutzerInnen verlangen nach einer Funktion, die es ihnen ermöglicht, Mahlzeiten direkt zu planen. Du hast jedoch nur begrenzte Ressourcen. Wie gehst du mit dieser Anfrage um?'
    '</div>',
    unsafe_allow_html=True
)

antworten = [
    "A: Du baust sofort die neue Funktion, ohne zu testen, ob die NutzerInnen sie wirklich wollen.",
    "B: Du verzichtest auf die Funktion, da du dich auf das Rezept-Feed konzentrieren möchtest.",
    "C: Du baust ein MVP der neuen Funktion und testest, ob sie tatsächlich ein Bedürfnis der Zielgruppe löst.",
    "D: Du baust eine Umfrage und fragst deine NutzerInnen, ob sie die Funktion nutzen würden."
]
feedback = [
    "Falsch. Ein sofortiges Bauen ohne Testen kann zu Ressourcenverschwendung führen. Du musst sicherstellen, dass die neue Funktion tatsächlich einen Mehrwert bietet.",
    "Falsch. Die Entscheidung, komplett auf die Funktion zu verzichten, könnte dazu führen, dass du auf einen potenziellen Vorteil verzichtest, der den Erfolg deiner App steigern könnte.",
    "Richtig! Du solltest ein MVP bauen, um mit minimalen Ressourcen herauszufinden, ob es wirklich Bedarf für die neue Funktion gibt.",
    "Falsch. Umfragen sind zwar hilfreich, aber sie geben dir nicht die praktischen Einblicke, die du benötigst, um eine fundierte Entscheidung zu treffen. Ein MVP ist hier effektiver."
]
richtige_antwort = 2  # Index für Antwort C

if "ld2_radio_key" not in st.session_state:
    st.session_state["ld2_radio_key"] = 0
if "ld2_abgegeben" not in st.session_state:
    st.session_state["ld2_abgegeben"] = False
if "ld2_feedback" not in st.session_state:
    st.session_state["ld2_feedback"] = None

auswahl = st.radio(
    "Antwort auswählen:",  # KORRIGIERT: Einfaches Label statt undefinierter Variable
    antworten,
    key=f"ld2_radio_{st.session_state['ld2_radio_key']}",
    disabled=st.session_state["ld2_abgegeben"]
)

if not st.session_state["ld2_abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["ld2_abgegeben"] = True
        if antworten.index(auswahl) == richtige_antwort:
            st.session_state["ld2_feedback"] = "richtig"
        else:
            st.session_state["ld2_feedback"] = "falsch"

if st.session_state["ld2_abgegeben"]:
    idx = antworten.index(auswahl)
    if st.session_state["ld2_feedback"] == "richtig":
        st.markdown(f'<div class="feedback-success">{feedback[idx]}</div>', unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("Weiter"):
            st.session_state["ld2_abgegeben"] = False
            st.session_state["ld2_radio_key"] += 1
            st.switch_page("pages/Abschluss.py")
    else:
        st.markdown(f'<div class="feedback-error">{feedback[idx]}</div>', unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("Wiederholen"):
            st.session_state["ld2_abgegeben"] = False
            st.session_state["ld2_radio_key"] += 1
            st.info("🔄 Gleich geht's weiter! Drücke erneut den Button Wiederholen.")
            st.rerun()
