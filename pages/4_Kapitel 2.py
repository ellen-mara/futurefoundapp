import streamlit as st

# --- Stil und Divider ---
st.markdown("""
    <style>
    .stApp { background: #23272f !important; }
    .main-title { font-size: 2.1em; font-weight: bold; color: #fff; text-align: center; margin-bottom: 0.3em;}
    .subtitle { color: #d9e0e7; font-size: 1.18em; margin-bottom: 1.4em; text-align: center; }
    .white-divider { height: 2px; width: 100%; background: #fff; margin: 32px 0 28px 0; border: none; border-radius: 2px; box-shadow: 0 1px 4px #0001; }
    .info-text { color: #e9ecef; font-size: 1.09em; margin-bottom: 1.2em; }
    .exkurs-box { background: #393e46; color: #fff; border-radius: 12px; padding: 1em 1.2em; margin-top: 1.2em; font-size: 1.01em; border-left: 6px solid #00adb5;}

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

st.markdown('<div class="main-title">Kapitel 2: Der Lean-Zyklus</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Build – Measure – Learn (BML)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Lernziel: Du kennst den BML-Zyklus und weisst, wie du mit einem MVP schnell und sinnvoll testest.</div>', unsafe_allow_html=True)
st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

# --- YouTube-Video: Lean Startup Explained (nur Build Measure Learn Cycle) ---
youtube_id = "xkaabHiZN-k"
start_seconds = 114  # 1:54 (1*60 + 54 = 114 Sekunden)
end_seconds = 480    # 8:00 (8*60 = 480 Sekunden)

embed_url = f"https://www.youtube.com/embed/{youtube_id}?start={start_seconds}&end={end_seconds}&controls=1"

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

# --- Quelle hinzufügen ---
st.markdown(
    '<div style="font-size:0.95em; font-style:italic; color:#bfc9d1; text-align:left; margin-top:0.2em;">'
    'Quelle: <a href="https://www.youtube.com/embed/xkaabHiZN-k?start=114&end=480&controls=1" style="color:#bfc9d1;" target="_blank">https://youtube.com</a>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="white-divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="info-text">'
    'Der Lean Ansatz hilft dabei, Annahmen nicht blind zu treffen, sondern testet, was Menschen wirklich brauchen. '
    'Stell dir vor, du möchtest eine App entwickeln, die Menschen hilft, sich nachhaltiger zu ernähren. '
    'Im ersten Schritt – <b>Build</b> – baust du ein MVP, also ein Minimum Viable Product. '
    'Das ist die einfachste funktionsfähige Version deiner App, zum Beispiel ein Rezept-Feed mit CO₂-Angaben. '
    'Im nächsten Schritt – <b>Measure</b> – misst du, wie echte NutzerInnen mit dem MVP interagieren: '
    'Welche Rezepte werden angeklickt? Wie oft wird die App geöffnet? '
    'Diese Daten helfen dir im dritten Schritt – <b>Learn</b> – herauszufinden, ob deine Idee wirklich ein Problem löst. '
    'Vielleicht stellst du fest, dass viele NutzerInnen zwar Rezepte mögen, aber nach Einkaufstipps suchen. '
    'Dann kannst du gezielt verbessern. Wichtig dabei: Es geht nicht um Likes oder oberflächliche Zustimmung, '
    'sondern um echte Erkenntnisse, die dein Produkt besser machen.'
    '</div>',
    unsafe_allow_html=True
)

# --- Klickbare Infopunkte ---
with st.expander("ℹ️ Was ist der Build-Measure-Learn-Zyklus?"):
    st.write(
        "Der Build-Measure-Learn-Zyklus ist das Herzstück des Lean-Startup-Ansatzes. "
        "Du entwickelst eine einfache Version deines Produkts (Build), misst das Nutzerverhalten (Measure) "
        "und lernst daraus (Learn), um gezielt zu verbessern."
    )

with st.expander("🛠️ Was ist ein MVP?"):
    st.write(
        "MVP steht für Minimum Viable Product. Das ist die minimal funktionsfähige Version deines Produkts, "
        "mit der du möglichst schnell und günstig testen kannst, ob deine Idee wirklich gebraucht wird."
    )

with st.expander("📊 Warum messen wir?"):
    st.write(
        "Nur durch Messen erfährst du, wie NutzerInnen wirklich mit deinem Produkt umgehen. "
        "So kannst du Annahmen überprüfen und gezielt weiterentwickeln."
    )

with st.expander("💡 Warum sind Learnings wichtiger als Likes?"):
    st.write(
        "Likes sind nett, aber sie sagen wenig darüber aus, ob dein Produkt wirklich ein Problem löst. "
        "Wichtiger sind echte Erkenntnisse aus dem Nutzerverhalten, damit du dein Produkt sinnvoll verbessern kannst."
    )

# --- Exkurs-Box ---
st.markdown(
    '<div class="exkurs-box">'
    '<b>Exkurs: Warum dieses Beispiel?</b><br>'
    'Nachhaltige Ernährung ist ein aktuelles, greifbares Thema mit hoher Alltagsnähe. Viele Menschen haben ein grundsätzliches Interesse daran – '
    'aber das Verhalten zeigt oft etwas anderes. Genau hier kommt der Lean-Ansatz ins Spiel: Statt Annahmen blind umzusetzen, testen wir, was Menschen wirklich brauchen. '
    'Das macht dieses Beispiel ideal, um die Logik des Lean-Startup-Denkens direkt verständlich zu machen.'
    '</div>',
    unsafe_allow_html=True
)

# --- Navigation ---
st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)  # vertikaler Abstand vor den Buttons

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("Zurück"):
        st.switch_page("pages/3_Kapitel 1_LK.py")
with col3:
    if st.button("Weiter"):
        st.switch_page("pages/5_Kapitel 2_LK.py")
