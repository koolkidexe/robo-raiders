import streamlit as st
import random

# --- Initialize state ---
if "initialized" not in st.session_state:
    st.session_state.islands = ["Island A", "Island B", "Island C", "Island D", "Island E"]
    st.session_state.correct_island = random.randint(0, 4)
    st.session_state.clues_found = [None] * 5
    st.session_state.excavated = [False] * 5
    st.session_state.turns = 10
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.message = "🌍 Welcome to the Archaeology Survey Game!"
    st.session_state.action_taken = False
    st.session_state.initialized = True

# --- Game functions ---
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
            ("🌱 Charcoal from ancient fire", 7),
            ("❌ Nothing significant", 0)
        ]
        find, points = random.choice(finds)
        st.session_state.score += points
        st.session_state.message = f"Excavation at {st.session_state.islands[island_index]}: {find} (+{points} points)"

    st.session_state.turns -= 1
    st.session_state.action_taken = True
    check_end()

def check_end():
    if st.session_state.turns <= 0 and not st.session_state.game_over:
        st.session_state.message += f"\n⏳ Out of time! The ruins remain undiscovered. Final Score: {st.session_state.score}"
        st.session_state.game_over = True

def reset_game():
    st.session_state.islands = ["Island A", "Island B", "Island C", "Island D", "Island E"]
    st.session_state.correct_island = random.randint(0, 4)
    st.session_state.clues_found = [None] * 5
    st.session_state.excavated = [False] * 5
    st.session_state.turns = 10
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.message = "🌍 New expedition started!"
    st.session_state.action_taken = False
    st.session_state.initialized = True

def next_turn():
    st.session_state.message = "Choose your next action."
    st.session_state.action_taken = False

# --- UI ---
st.title("🏝️ Archaeology Survey Game")
st.markdown("Help an archaeologist survey 5 islands and uncover the lost ruins. You have **10 turns**!")

# Sidebar for stats
st.sidebar.header("📊 Expedition Status")
st.sidebar.write(f"⭐ Score: **{st.session_state.score}**")
st.sidebar.write(f"⏳ Turns Left: **{st.session_state.turns}**")

if st.sidebar.button("🔄 Restart Game"):
    reset_game()

# --- Instructions ---
with st.expander("ℹ️ How to Play"):
    st.markdown("""
    **Your Mission**: Find the hidden ruins on one of 5 islands before you run out of turns!

    - **Survey** 🔎 → Searches the surface.  
      - 🏺 *Ruins markings*: You are on the correct island!  
      - 🔎 *Pottery fragments*: Ruins are very close.  
      - 🦴 *Bones*: Some activity nearby, but ruins are further away.  
      - 🌊 *Shells and sand*: Nothing important nearby.  

    - **Excavate** ⛏ → Digs deeper into the island.  
      - If it's the correct island, you win **100 points** and find the ruins! 🎉  
      - If not, you may still find **artifacts** worth points (tools, pottery, bones, charcoal).  

    **Turns**: Each action (Survey or Excavate) uses 1 turn. You start with **10 turns**.  
    """)

# Show message
st.info(st.session_state.message)

# Action buttons (only if no action taken yet and game not over)
if not st.session_state.game_over:
    if not st.session_state.action_taken:
        st.subheader("Choose an action")
        for i, name in enumerate(st.session_state.islands):
            col1, col2 = st.columns(2)
            with col1:
                st.button(f"Survey {name}", key=f"survey_{i}", on_click=survey, args=(i,))
            with col2:
                st.button(f"Excavate {name}", key=f"excavate_{i}", on_click=excavate, args=(i,))
    else:
        # Show "Next Turn" button
        st.button("➡️ Next
