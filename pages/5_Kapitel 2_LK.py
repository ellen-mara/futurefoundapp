import streamlit as st

# --- Stil und Schrittzähler ---
st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.18em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .stepper-wrap { display: flex; justify-content: center; align-items: center; margin: 1.2em 0 2em 0; }
    .stepper-ball { width: 32px; height: 32px; border-radius: 50%; background: #393e46; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.15em; margin: 0 8px; border: 2.5px solid #393e46; transition: background 0.2s, color 0.2s; }
    .stepper-ball.active { background: #00adb5; color: #23272f; border: 2.5px solid #fff; box-shadow: 0 0 0 4px #00adb522; }
    .stepper-ball.done { background: linear-gradient(135deg, #00adb5 70%, #393e46 100%); color: #fff; border: 2.5px solid #00adb5; }
    .stepper-bar { flex: 1; height: 6px; background: #393e46; border-radius: 3px; margin: 0 3px; position: relative; min-width: 28px; max-width: 70px; }
    .stepper-bar-fill { height: 100%; background: #00adb5; border-radius: 3px; position: absolute; left: 0; top: 0; transition: width 0.3s; }
    .szenario-box { background: #393e46; color: #fff; border-radius: 12px; padding: 1.1em 1.4em; margin: 1.3em 0 1.3em 0; border-left: 6px solid #00adb5; font-size: 1.05em; }

    /* Erzwinge dein aktuelles Theme auf allen Geräten */
    .stApp {
        background-color: #23272f !important;
        color: #ffffff !important;
    }
    
    /* Überschreibe System-Theme-Preferences */
    @media (prefers-color-scheme: light), (prefers-color-scheme: dark) {
        .stApp {import streamlit as st

# --- Stil und Schrittzähler ---
st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.18em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .stepper-wrap { display: flex; justify-content: center; align-items: center; margin: 1.2em 0 2em 0; }
    .stepper-ball { width: 32px; height: 32px; border-radius: 50%; background: #393e46; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.15em; margin: 0 8px; border: 2.5px solid #393e46; transition: background 0.2s, color 0.2s; }
    .stepper-ball.active { background: #00adb5; color: #23272f; border: 2.5px solid #fff; box-shadow: 0 0 0 4px #00adb522; }
    .stepper-ball.done { background: linear-gradient(135deg, #00adb5 70%, #393e46 100%); color: #fff; border: 2.5px solid #00adb5; }
    .stepper-bar { flex: 1; height: 6px; background: #393e46; border-radius: 3px; margin: 0 3px; position: relative; min-width: 28px; max-width: 70px; }
    .stepper-bar-fill { height: 100%; background: #00adb5; border-radius: 3px; position: absolute; left: 0; top: 0; transition: width 0.3s; }
    .szenario-box { background: #393e46; color: #fff; border-radius: 12px; padding: 1.1em 1.4em; margin: 1.3em 0 1.3em 0; border-left: 6px solid #00adb5; font-size: 1.05em; }

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

def stepper(current, total):
    balls = []
    for i in range(total):
        ball_class = "stepper-ball"
        if i < current:
            ball_class += " done"
        elif i == current:
            ball_class += " active"
        balls.append(f'<div class="{ball_class}">{i+1}</div>')
    bars = []
    for i in range(total-1):
        fill = "100%" if i < current else "0%"  # HIER WAR DER FEHLER - fehlte: else "0%"
        bars.append(f'<div class="stepper-bar"><div class="stepper-bar-fill" style="width:{fill};"></div></div>')
    html = '<div class="stepper-wrap">'
    for i in range(total):
        html += balls[i]
        if i < total-1:
            html += bars[i]
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# --- Fragen und Feedback, inkl. Szenario als 4. Punkt ---
fragen = [
    {
        "frage": "Wofür steht die Abkürzung BML im Lean-Startup-Ansatz?",
        "antworten": [
            "Brainstorm – Market – Launch",
            "Business – Model – Launch",
            "Budget – Marketing – Learning",
            "Build – Measure – Learn"
        ],
        "richtig": 3,
        "feedback_richtig": "Genau!",
        "feedback_falsch": "Probier es nochmals!"
    },
    {
        "frage": "Was beschreibt den Lean-Ansatz im Sinne von Build – Measure – Learn (BML)?",
        "antworten": [
            "Möglichst günstig ein Produkt entwickeln und verkaufen",
            "Schnell ein vollständiges Produkt bauen und intensiv bewerben",
            "Ideen schrittweise testen, Daten sammeln und daraus lernen",
            "Einmal planen und dann konsequent umsetzen"
        ],
        "richtig": 2,
        "feedback_richtig": "Genau!",
        "feedback_falsch": "Probier es nochmals!"
    },
    {
        "frage": "Wofür steht MVP (Minimum Viable Product) im Lean-Startup-Kontext?",
        "antworten": [
            "Es handelt sich um das fertige, ausgereifte Produkt, das alle Features umfasst.",
            "Es ist das minimal funktionsfähige Produkt, um die wichtigsten Annahmen zu testen und Feedback zu erhalten.",
            "Es ist das teuerste und umfangreichste Produkt, das den gesamten Markt ansprechen soll.",
            "Es ist ein Prototyp, der nur intern verwendet wird, um technische Lösungen zu validieren."
        ],
        "richtig": 1,
        "feedback_richtig": "Genau!",
        "feedback_falsch": "Probier es nochmals!"
    },
    {
        "szenario": True,
        "frage": "FutureFound hat ein MVP released – 100 Downloads, aber kaum aktive Nutzung.",
        "aufgabe": "Wie gehst du vor?",
        "antworten": [
            "Neues Feature entwickeln",
            "NutzerInnen interviewen",
            "Werbung schalten",
            "Produkt stoppen"
        ],
        "richtig": 1,
        "feedback_richtig": "Richtig! NutzerInnen zu interviewen ist der beste Weg, um herauszufinden, warum das Produkt nicht genutzt wird. Jetzt bekommen wir echte Einblicke, was fehlt oder nicht passt.",
        "feedback_falsch": "Das ist nicht die beste Wahl. Es ist wichtig, zuerst zu verstehen, warum die NutzerInnen nicht aktiv sind."
    }
]

# --- Session State für Quiz ---
if "k2_frage_idx" not in st.session_state:
    st.session_state["k2_frage_idx"] = 0
if "k2_abgegeben" not in st.session_state:
    st.session_state["k2_abgegeben"] = False
if "k2_feedback" not in st.session_state:
    st.session_state["k2_feedback"] = None
if "k2_radio_key" not in st.session_state:
    st.session_state["k2_radio_key"] = 0

# --- Fehlerbehandlung für Index ---
aktuelle_frage = min(st.session_state["k2_frage_idx"], len(fragen)-1)
gesamt_fragen = len(fragen)

# --- Titel, Stepper, Divider ---
st.markdown('<div class="main-title">Kapitel 2: Der Lean-Zyklus</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Build – Measure – Learn (BML)</div>', unsafe_allow_html=True)
stepper(aktuelle_frage, gesamt_fragen)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# --- Frage oder Szenario anzeigen ---
frage = fragen[aktuelle_frage]

if "szenario" in frage and frage["szenario"]:
    st.markdown(f'<div class="szenario-box"><b>Szenario:</b> {frage["frage"]}</div>', unsafe_allow_html=True)
    st.markdown(f"<b>{frage['aufgabe']}</b>", unsafe_allow_html=True)
else:
    st.markdown(f"<b>{frage['frage']}</b>", unsafe_allow_html=True)

auswahl = st.radio(
    "Antwort auswählen:",
    frage["antworten"],
    key=f"k2_radio_{st.session_state['k2_radio_key']}_{aktuelle_frage}",
    disabled=st.session_state["k2_abgegeben"]
)

# --- Abgabe-Button ---
if not st.session_state["k2_abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["k2_abgegeben"] = True
        if frage["antworten"].index(auswahl) == frage["richtig"]:
            st.session_state["k2_feedback"] = "richtig"
        else:
            st.session_state["k2_feedback"] = "falsch"
        st.rerun()

# --- Feedback & Navigation ---
if st.session_state["k2_abgegeben"]:
    if st.session_state["k2_feedback"] == "richtig":
        st.success(frage["feedback_richtig"])
        if aktuelle_frage < gesamt_fragen-1:
            if st.button("Weiter"):
                st.session_state["k2_frage_idx"] += 1
                st.session_state["k2_abgegeben"] = False
                st.session_state["k2_feedback"] = None
                st.session_state["k2_radio_key"] += 1
                st.rerun()
        else:
            if st.button("Weiter"):
                st.session_state["k2_frage_idx"] = 0
                st.session_state["k2_abgegeben"] = False
                st.session_state["k2_feedback"] = None
                st.session_state["k2_radio_key"] += 1
                st.switch_page("pages/6_Kapitel 3.py")  # Anpassen an deine nächste Seite
                
    else:
        st.error(frage["feedback_falsch"])
        if st.button("Wiederholen"):
            st.session_state["k2_abgegeben"] = False
            st.session_state["k2_feedback"] = None
            st.session_state["k2_radio_key"] += 1
            st.rerun()

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

def stepper(current, total):
    balls = []
    for i in range(total):
        ball_class = "stepper-ball"
        if i < current:
            ball_class += " done"
        elif i == current:
            ball_class += " active"
        balls.append(f'<div class="{ball_class}">{i+1}</div>')
    bars = []
    for i in range(total-1):
        fill = "100%" if i < current
