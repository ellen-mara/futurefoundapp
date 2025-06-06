import streamlit as st

st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.15em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .info-text { color: #e9ecef; font-size: 1.09em; margin-bottom: 1.2em; }

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

st.markdown('<div class="main-title">Kapitel 4: Lean Denken in Entscheidungen</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Kundeninterview oder Datenanalyse?</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="info-text">'
    'Der Lean Startup-Ansatz basiert auf der Vorstellung, dass es wichtig ist, schnell zu handeln, Fehler zu machen und daraus zu lernen. '
    'Du kannst nicht immer alles von Anfang an perfekt planen – manchmal musst du die Dinge einfach ausprobieren und anhand der Ergebnisse entscheiden, wie du weitermachst.<br><br>'
    'In einer dynamischen Start-up-Welt ist es entscheidend, nicht in langen Planungsphasen festzustecken, sondern schnell zu handeln, zu messen und zu lernen. '
    'Das bedeutet, du wirst Entscheidungen häufig auf Basis von Experimenten treffen.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("<div style='height: 44px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 6, 1], gap="small")
with col1:
    if st.button("Zurück"):
        st.switch_page("pages/7_Kapitel 3_LK.py")
with col3:
    if st.button("Weiter"):
        st.switch_page("pages/9_Kapitel 4_LK Teil 1.py")
