import streamlit as st
import random

# --- Initialize game state ---
if "initialized" not in st.session_state:
    st.session_state.turns = 10
    st.session_state.funds = 50  # starting money
    st.session_state.artifacts = 0
    st.session_state.message = "Welcome! You’re managing an archaeology expedition. Raise money and discover artifacts!"
    st.session_state.game_over = False
    st.session_state.initialized = True

def reset_game():
    st.session_state.turns = 10
    st.session_state.funds = 50
    st.session_state.artifacts = 0
    st.session_state.message = "New expedition started!"
    st.session_state.game_over = False

def fundraise():
    if st.session_state.turns <= 0 or st.session_state.game_over:
        return
    raised = random.randint(5, 20)
    st.session_state.funds += raised
    st.session_state.message = f"📢 You held a fundraiser and raised **${raised}**!"
    end_turn()

def excavate():
    if st.session_state.turns <= 0 or st.session_state.game_over:
        return
    if st.session_state.funds < 15:
        st.session_state.message = "⚠️ Not enough funds to excavate. Try fundraising instead!"
        return
    st.session_state.funds -= 15
    finds = [
        ("🪨 Broken pottery", 1),
        ("🪓 Ancient tool", 2),
        ("🦴 Human bones", 2),
        ("🏺 Rare vase", 5),
        ("❌ Nothing found", 0)
    ]
    find, points = random.choice(finds)
    st.session_state.artifacts += points
    st.session_state.message = f"⛏️ Excavation success! You found: {find} (+{points} artifacts)"
    end_turn()

def educate():
    if st.session_state.turns <= 0 or st.session_state.game_over:
        return
    gained = random.randint(3, 10)
    st.session_state.funds += gained
    st.session_state.message = f"🎓 You ran a school program and gained **${gained}** in donations!"
    end_turn()

def end_turn():
    st.session_state.turns -= 1
    if st.session_state.turns <= 0:
        if st.session_state.artifacts >= 8 and st.session_state.funds >= 10:
            st.session_state.message = (
                f"🏆 You won! You collected **{st.session_state.artifacts} artifacts** "
                f"and ended with **${st.session_state.funds}**.\n\n"
                f"📍 Here are the coordinates: **(41º43'27'' N, 72º33'55'' W)**"
            )
        else:
            st.session_state.message = (
                f"⏳ Expedition over! You collected **{st.session_state.artifacts} artifacts** "
                f"and ended with **${st.session_state.funds}**."
            )
        st.session_state.game_over = True

# --- UI ---
st.title("🏛️ Archaeology Expedition: Funding Challenge")
st.markdown("Your mission is to raise money and help archaeologists make discoveries!")

# 📘 How to Play dropdown
with st.expander("ℹ️ How to Play"):
    st.markdown("""
    🎮 **Goal:**  
    Complete your 10-turn expedition with at least **8 artifacts** and at least **$10** to win.  
    If you succeed, you’ll unlock the coordinates to the geocache!

    **Actions:**
    - 🪙 **Fundraise** → Gain random funds ($5–20)  
    - 🎓 **Educate Schools** → Gain smaller, steady donations ($3–10)  
    - ⛏️ **Excavate** → Costs $15, find 0–5 artifacts  

    Each action costs **1 turn**.  
    You start with **$50** and **10 turns**.
    """)

# Sidebar info
st.sidebar.header("📊 Expedition Status")
st.sidebar.write(f"💰 Funds: **${st.session_state.funds}**")
st.sidebar.write(f"🏺 Artifacts: **{st.session_state.artifacts}**")
st.sidebar.write(f"⏳ Turns left: **{st.session_state.turns}**")

if st.sidebar.button("🔄 Restart Game"):
    reset_game()

# --- Game message display ---
if st.session_state.game_over and st.session_state.artifacts >= 8 and st.session_state.funds >= 10:
    st.success(st.session_state.message)
else:
    st.info(st.session_state.message)

# --- Action buttons ---
if not st.session_state.game_over:
    st.subheader("Choose your action")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📢 Fundraise", on_click=fundraise)
    with col2:
        st.button("⛏️ Excaviate", on_click=excavate)
    with col3:
        st.button("🎓 Educate Schools", on_click=educate)

# --- Educational info ---
with st.expander("💡 Why funding matters"):
    st.markdown("""
    Archaeologists need money for:
    - 🔨 Excavation tools  
    - 🚐 Transportation  
    - 🧑‍🔬 Lab work  
    - 📚 Education programs  
    
    Without funding:
    - 🚫 Sites go unexplored  
    - 🏺 Artifacts decay or get looted  
    - 🧩 History is lost forever  
    """)
