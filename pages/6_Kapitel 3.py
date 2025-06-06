import streamlit as st

st.markdown("""
    <style>
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


# Session-State für Reset beim Seitenaufruf
if "kapitel1_visited" not in st.session_state:
    for idx in range(4):
        st.session_state[f"tile_{idx}_clicked"] = False
    st.session_state["kapitel1_visited"] = True

st.title("Startup Lean-Up! Vom Produkt zur validierten Problemhypothese")
st.markdown('<div class="subtitle">Lernziel: Du lernst warum es entscheidend ist, zuerst das Problem zu verstehen – nicht das Produkt zu bauen.</div>', unsafe_allow_html=True)


# --- Szenario-Box (neu hinzugefügt, fett für die letzte Zeile) ---
st.markdown("""
    <style>
    .szenario-box {
        background: #393e46;
        color: #fff;
        border-radius: 12px;
        padding: 1.1em 1.4em;
        margin: 1.3em 0 1.3em 0;
        border-left: 6px solid #00adb5;
        font-size: 1.05em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="szenario-box">'
    'Viele Startups scheitern nicht an der Technologie – sondern daran, dass sie ein Produkt für ein Problem entwickeln, das niemand hat.<br>'
    'Lean Startup kehrt diese Logik um:</b><br>'
    '<b><u>Nicht zuerst entwickeln – sondern zuerst verstehen.</b>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("<div style='height: 44px;'></div>", unsafe_allow_html=True)

# --- YouTube-Video (nur von 0:00 bis 2:40 abspielbar) ---
youtube_id = "dQw4w9WgXcQ"  # Ersetze durch die ID deines Videos!
start_seconds = 0
end_seconds = 160  # 2 Minuten 40 Sekunden

embed_url = f"https://www.youtube.com/embed/wXc-SWqBnKc?start=0&end=160&controls=1"

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <iframe width="700" height="394"
        src="{embed_url}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Vertikaler Abstand vor den Buttons ---
st.markdown("<div style='height: 44px;'></div>", unsafe_allow_html=True)

# --- Navigation mit drei Spalten, Buttons links/rechts ---
col1, col2, col3 = st.columns([1, 6, 1], gap="small")

with col1:
    if st.button("Zurück", key="zurueck"):
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("5_Kapitel 2_LK.py")
with col3:
    if st.button("Weiter", key="weiter"):
        for idx in range(4):
            st.session_state[f"tile_{idx}_clicked"] = False
        st.session_state["kapitel1_visited"] = False
        st.switch_page("pages/7_Kapitel 3_LK.py")
