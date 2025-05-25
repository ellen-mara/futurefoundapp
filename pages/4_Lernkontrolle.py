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
        fill = "100%" if i < current else "0%"
        bars.append(f'<div class="stepper-bar"><div class="stepper-bar-fill" style="width:{fill};"></div></div>')
    html = '<div class="stepper-wrap">'
    for i in range(total):
        html += balls[i]
        if i < total-1:
            html += bars[i]
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# --- Beispiel-Fragen und Feedback für page4_Lernkontrolle ---
fragen = [
    {
        "frage": "Was beschreibt den Kern des Lean-Startup-Ansatzes?",
        "antworten": [
            "Mit möglichst wenig Geld ein Unternehmen gründen.",
            "Schnell zu lernen und das Geschäftsmodell anzupassen.",
            "Nur für Tech-Startups geeignet.",
            "Einen festen Plan verfolgen."
        ],
        "richtig": 1,
        "feedback_richtig": "✅ Richtig! Lean Startup bedeutet, schnell zu lernen.",
        "feedback_falsch": "❌ Fast! Denk nochmal an das Build-Measure-Learn-Prinzip."
    },
    {
        "frage": "Was ist ein MVP (Minimum Viable Product)?",
        "antworten": [
            "Ein Produkt mit allen Features.",
            "Die minimal funktionsfähige Version, um Annahmen zu testen.",
            "Ein Produkt, das nur intern genutzt wird.",
            "Ein Produkt, das sofort an alle verkauft wird."
        ],
        "richtig": 1,
        "feedback_richtig": "✅ Richtig! Ein MVP ist die einfachste Version, um schnell zu testen.",
        "feedback_falsch": "❌ Das ist nicht korrekt. Überleg nochmal, was ein MVP leisten soll."
    }
    # Weitere Fragen nach Bedarf ergänzen!
]

# --- Session State für Quiz ---
if "k4_frage_idx" not in st.session_state:
    st.session_state["k4_frage_idx"] = 0
if "k4_abgegeben" not in st.session_state:
    st.session_state["k4_abgegeben"] = False
if "k4_feedback" not in st.session_state:
    st.session_state["k4_feedback"] = None
if "k4_radio_key" not in st.session_state:
    st.session_state["k4_radio_key"] = 0
if "k4_reset_pending" not in st.session_state:
    st.session_state["k4_reset_pending"] = False

# --- Reset-Logik ---
def reset_frage():
    st.session_state["k4_abgegeben"] = False
    st.session_state["k4_feedback"] = None
    st.session_state["k4_radio_key"] += 1

def reset_pending():
    st.session_state["k4_reset_pending"] = True

if st.session_state["k4_reset_pending"]:
    reset_frage()
    st.session_state["k4_reset_pending"] = False

# --- Fehlerbehandlung für Index ---
aktuelle_frage = min(st.session_state["k4_frage_idx"], len(fragen)-1)
gesamt_fragen = len(fragen)

# --- Titel, Stepper, Divider ---
st.markdown('<div class="main-title">Kapitel 4: Lernkontrolle</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Teste dein Wissen zum Lean-Startup-Ansatz!</div>', unsafe_allow_html=True)
stepper(aktuelle_frage, gesamt_fragen)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# --- Frage anzeigen ---
frage = fragen[aktuelle_frage]
st.markdown(f"<b>{frage['frage']}</b>", unsafe_allow_html=True)

auswahl = st.radio(
    "Antwort auswählen:",
    frage["antworten"],
    key=f"k4_radio_{st.session_state['k4_radio_key']}_{aktuelle_frage}",
    disabled=st.session_state["k4_abgegeben"]
)

# --- Abgabe-Button ---
if not st.session_state["k4_abgegeben"]:
    if st.button("Abgabe"):
        st.session_state["k4_abgegeben"] = True
        if frage["antworten"].index(auswahl) == frage["richtig"]:
            st.session_state["k4_feedback"] = "richtig"
        else:
            st.session_state["k4_feedback"] = "falsch"

# --- Feedback & Navigation ---
if st.session_state["k4_abgegeben"]:
    if st.session_state["k4_feedback"] == "richtig":
        st.success(frage["feedback_richtig"])
        if aktuelle_frage < gesamt_fragen-1:
            if st.button("Weiter"):
                st.session_state["k4_frage_idx"] += 1
                reset_frage()
        else:
            if st.button("Zurück zu Kapitelübersicht"):
                st.session_state["k4_frage_idx"] = 0
                reset_frage()
                st.switch_page("pages/6_Kapitelübersicht.py")
    else:
        st.error(frage["feedback_falsch"])
        if st.button("Wiederholen"):
            reset_pending()
            st.info("🔄 Gleich geht's weiter! Die Frage wird jetzt neu geladen ...")
