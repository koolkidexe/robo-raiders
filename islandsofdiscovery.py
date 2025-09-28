import streamlit as st
import random

# --- Initialize state ---
if "initialized" not in st.session_state:
    st.session_state.islands = ["Island A", "Island B", "Island C", "Island D", "Island E"]
    st.session_state.correct_island = random.randint(0, 4)
    st.session_state.clues_found = [None] * 5
    st.session_state.excavated = [False] * 5
    st.session_state.turns = 5
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.message = "🌍 Welcome to Islands of Discovery!"
    st.session_state.action_taken = False
    st.session_state.initialized = True

# --- Game functions ---
def survey(island_index):
    distance = abs(island_index - st.session_state.correct_island)
    if distance == 0:
        clue = "🏺 Ruins markings"
    elif distance == 1:
        clue = "🔎 Pottery fragments"
    elif distance == 2:
        clue = "🦴 Ancient bones"
    else:
        clue = "🌊 Just shells"
    st.session_state.clues_found[island_index] = clue
    st.session_state.message = f"Survey at {st.session_state.islands[island_index]}: {clue}"
    st.session_state.turns -= 1
    st.session_state.action_taken = True
    check_end()

def excavate(island_index):
    if st.session_state.excavated[island_index]:
        st.session_state.message = f"You already excavated {st.session_state.islands[island_index]}."
        st.session_state.action_taken = True
        return

    st.session_state.excavated[island_index] = True

    if island_index == st.session_state.correct_island:
        st.session_state.score += 100
        st.session_state.message = f"🎉 You excavated {st.session_state.islands[island_index]} and found the ruins! 🏆 Final Score: {st.session_state.score}"
        st.session_state.game_over = True
    else:
        finds = [
            ("🪨 Broken pottery shard", 5),
            ("🪓 Old stone tool", 10),
            ("🦴 Animal bones", 3),
            ("🌱 Charcoal remains",
