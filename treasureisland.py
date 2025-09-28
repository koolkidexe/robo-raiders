import streamlit as st
import random

# --- Initialize state ---
if "initialized" not in st.session_state:
    st.session_state.map_size = 5
    st.session_state.t_row = random.randint(0, st.session_state.map_size - 1)
    st.session_state.t_column = random.randint(0, st.session_state.map_size - 1)
    st.session_state.game_map = [["🏝" for _ in range(st.session_state.map_size)] for _ in range(st.session_state.map_size)]
    st.session_state.game_over = False
    st.session_state.message = "Welcome to Treasure Island! Find the hidden treasure."
    st.session_state.initialized = True

def reset_game():
    st.session_state.t_row = random.randint(0, st.session_state.map_size - 1)
    st.session_state.t_column = random.randint(0, st.session_state.map_size - 1)
    st.session_state.game_map = [["🏝" for _ in range(st.session_state.map_size)] for _ in range(st.session_state.map_size)]
    st.session_state.game_over = False
    st.session_state.message = "New game started! Find the hidden treasure."

def guess(row, col):
    if st.session_state.game_over:
        return

    if row == st.session_state.t_row and col == st.session_state.t_column:
        st.session_state.game_map[row][col] = "🪙"
        st.session_state.message = "🎉 You found the treasure! You win!"
        st.session_state.game_over = True
    else:
        if st.session_state.game_map[row][col] == "☠":
            st.session_state.message = "⚠️ You already searched there! Try a new island."
        else:
            st.session_state.game_map[row][col] = "☠"
            st.session_state.message = "❌ No treasure here! Keep searching."

# --- UI ---
st.title("🏝️ Treasure Island")
st.markdown("You are tasked with finding buried treasure on one of these islands! Tap to search.")

st.info(st.session_state.message)

# Render grid as buttons
for i in range(st.session_state.map_size):
    cols = st.columns(st.session_state.map_size)
    for j in range(st.session_state.map_size):
        with cols[j]:
            st.button(
                st.session_state.game_map[i][j],
                key=f"{i}_{j}",
                on_click=guess,
                args=(i, j),
                disabled=st.session_state.game_over
            )

st.sidebar.header("⚙️ Controls")
if st.sidebar.button("🔄 Restart Game"):
    reset_game()
