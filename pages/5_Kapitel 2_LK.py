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
        fill = "100%" if i < current
