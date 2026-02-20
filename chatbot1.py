import streamlit as st
import ollama
import time

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Captain Cool Chat",
    page_icon="🧢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🎨 Added Premium Animation + Stadium Theme UI
st.markdown("""
<style>

/* ---------------- GLOBAL THEME ---------------- */
html, body, [class*="css"]  {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Poppins', sans-serif;
    color: white;
}

/* ---------------- Animated Background Glow ---------------- */
body::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    top: -50%;
    left: -50%;
    background: radial-gradient(circle at center, rgba(255,215,0,0.08), transparent 40%);
    animation: rotateGlow 15s linear infinite;
    z-index: -1;
}

@keyframes rotateGlow {
    from {transform: rotate(0deg);}
    to {transform: rotate(360deg);}
}

/* ---------------- Glassmorphism Chat Box ---------------- */
.stChatMessage {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 10px;
    border: 1px solid rgba(255, 215, 0, 0.2);
    transition: 0.3s ease-in-out;
}

.stChatMessage:hover {
    transform: scale(1.02);
    border: 1px solid gold;
}

/* ---------------- Animated Logo ---------------- */
.logo-container {
    text-align: center;
    margin-bottom: 10px;
    animation: fadeIn 2s ease-in-out;
}

.logo {
    font-size: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, gold, white, gold);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s infinite linear;
}

@keyframes shine {
    0% { background-position: -200px; }
    100% { background-position: 200px; }
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* ---------------- Input Box Styling ---------------- */
.stChatInput input {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid gold !important;
}

/* ---------------- Smooth Button Hover ---------------- */
button:hover {
    background-color: gold !important;
    color: black !important;
    transition: 0.3s;
}

</style>
""", unsafe_allow_html=True)


# 🎨 Added Premium Animated Logo Section
st.markdown("""
<div class="logo-container">
    <div class="logo">🏏 CAPTAIN COOL AI 🧢</div>
    <p style="color:lightgray;">Calm. Tactical. Finisher Mindset.</p>
</div>
""", unsafe_allow_html=True)

st.title("🧢 Captain Cool Chat")
st.write("Chat with MS Dhoni style personality")

# ---------------------------
# Initialize Chat History ONCE
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are MS Dhoni, former captain of Indian cricket team.

Personality Rules:
- Speak calmly and confidently.
- Be humble and grounded.
- Give practical advice.
- Use simple language.
- Sometimes use cricket analogies.
- Stay emotionally balanced.
- Never say you are an AI.
- Reply like Dhoni himself is speaking.

🔥 Added MS Dhoni Personality Layer:
- Add slight motivational tone.
- Sound like a leader guiding his team.
- Occasionally reference match situations, chasing targets, field placements.
- Keep answers medium length.
- Make replies interactive and pleasant.
- Always maintain composure.
"""
        }
    ]

# ---------------------------
# Display Previous Messages
# ---------------------------
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# ---------------------------
# User Input Box
# ---------------------------
user_input = st.chat_input("Ask Captain Cool something...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # 🎨 Added Captain Entry Loading Animation
    with st.chat_message("assistant"):
        with st.spinner("🧢 Captain walking to the crease..."):
            time.sleep(1.5)

        response = ollama.chat(
            model="gemma3:latest",
            messages=st.session_state.messages
        )

        reply = response["message"]["content"]

        # Add assistant reply
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        st.write(reply)

# ---------------------------
# Footer - Finisher Mindset
# ---------------------------
st.markdown("""
<hr style="border: 0.5px solid rgba(255,215,0,0.2);">
<center style="color:gray;">
Built with composure, patience & finishing mindset 🏏 <br>
"Trust the process. Results will follow."
</center>
""", unsafe_allow_html=True)
