import streamlit as st

st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; }
    .subtitle { color: #d9e0e7; font-size: 1.15em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .info-text { color: #e9ecef; font-size: 1.09em; margin-bottom: 1.2em; }
    .merk-box { background: #393e46; color: #fff; border-radius: 12px; padding: 1.1em 1.4em; margin: 1.3em 0 1.3em 0; border-left: 6px solid #00adb5; font-size: 1.05em; }

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
st.markdown('<div class="subtitle">Den richtigen Moment für eine Entscheidung wählen</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="info-text">'
    'Du bist in der Entwicklung deines Produkts, und jetzt steht eine wichtige Entscheidung an: Sollst du dein Produkt verbessern, indem du neue Funktionen hinzufügst, oder lieber deine bestehenden Features optimieren und die Nutzererfahrung verbessern?'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="merk-box">'
    '<b>Wichtige Überlegung:</b><br>'
    'Der Lean-Ansatz fordert dich dazu auf, nicht sofort alles zu perfektionieren. Stattdessen solltest du die aktuellen Lernziele in den Vordergrund stellen und mit einem kleinen Schritt fortfahren, der dir echte, validierte Daten liefert. Auf diese Weise vermeidest du, unnötige Zeit und Ressourcen in Features zu investieren, die am Ende nicht genutzt werden.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("<div style='height: 44px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 6, 1], gap="small")
with col1:
    if st.button("Zurück"):
        st.switch_page("pages/9_Kapitel 4_LK Teil 1.py")
with col3:
    if st.button("Weiter"):
        st.switch_page("pages/11_Kapitel 4_LK Teil 2.py")
