import streamlit as st
import random

# --- Setup state ---
if "initialized" not in st.session_state:
    st.session_state.islands = ["Island A", "Island B", "Island C", "Island D", "Island E"]
    st.session_state.correct_island = random.randint(0, 4)
    st.session_state.clues_found = [None] * 5
    st.session_state.excavated = [False] * 5
    st.session_state.turns = 10
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.message = "🌍 Welcome to the Archaeology Survey Game!"

# --- Functions ---
def survey(island_index):
    distance = abs(island_index - st.session_state.correct_island)
    if distance == 0:
        clue = "🏺 Ruins markings on the surface!"
    elif distance == 1:
        clue = "🔎 Pottery fragments scattered around."
    elif distance == 2:
        clue = "🦴 Ancient bones buried shallowly."
    else:
        clue = "🌊 Just shells and sand."
    st.session_state.clues_found[island_index] = clue
    st.session_state.message = f"Survey results for {st.session_state.islands[island_index]}: {clue}"

def excavate(island_index):
    if st.session_state.excavated[island_index]:
        st.session_state.message = f"You already excavated {st.session_state.islands[island_index]}. Nothing new."
        return

    st.session_state.excavated[island_index] = True

    if island_index == st.session_state.correct_island:
        st.session_state.score += 100
        st.session_state.message = f"🎉 You excavated {st.session_state.islands[island_index]} and discovered the ancient ruins! 🏆 Final Score: {st.session_state.score}"
        st.session_state.game_over = True
    else:
        finds = [
            ("🪨 Broken pottery shard", 5),
            ("🪓 Old stone tool", 10),
            ("🦴 Animal bones", 3),
            ("🌱 Charcoal from ancient fire", 7),
            ("❌ Nothing significant", 0)
        ]
        find, points = random.choice(finds)
        st.session_state.score += points
        st.session_state.message = f"Excavation at {st.session_state.islands[island_index]}: {find} (+{points} points)"

    st.session_state.turns -= 1
    if st.session_state.turns <= 0 and not st.session_state.game_over:
        st.session_state.message += f"\n⏳ You ran out of time! The ruins remain undiscovered... Final Score: {st.session_state.score}"
        st.session_state.game_over = True

# --- UI ---
st.title("🏝️ Archaeology Survey Game")
st.write("Help an archaeologist survey 5 islands and find the lost ruins. You have 10 turns!")

st.write(f"⭐ Current Score: {st.session_state.score}")
st.write(f"⏳ Turns Remaining: {st.session_state.turns}")

st.info(st.session_state.message)

if not st.session_state.game_over:
    for i, name in enumerate(st.session_state.islands):
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Survey {name}", key=f"survey_{i}"):
                survey(i)
        with col2:
            if st.button(f"Excavate {name}", key=f"excavate_{i}"):
                excavate(i)

# Expedition Notes
st.subheader("📜 Expedition Notes")
for i, name in enumerate(st.session_state.islands):
    status = []
    if st.session_state.clues_found[i]:
        status.append(st.session_state.clues_found[i])
    if st.session_state.excavated[i]:
        status.append("⛏ Excavated")
    if not status:
        status.append("Unknown")
    st.write(f"- {name}: {' | '.join(status)}")
