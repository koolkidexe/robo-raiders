import random

# --- Setup ---
islands = ["Island A", "Island B", "Island C", "Island D", "Island E"]
correct_island = random.randint(0, 4)

# Track state
clues_found = [None] * 5   # stores clues after survey
excavated = [False] * 5    # has the island been excavated?
turns = 10                 # limited number of turns
score = 0                  # points from artifacts

print("🌍 Welcome to the Archaeology Survey Game!")
print("You are helping an archaeologist search 5 islands for the lost ruins.")
print("You have 10 turns to survey and excavate wisely!\n")

def survey(island_index):
    #Check surface clues based on distance from ruins
    distance = abs(island_index - correct_island)
    if distance == 0:
        clue = "🏺 Ruins markings on the surface!"
    elif distance == 1:
        clue = "🔎 Pottery fragments scattered around."
    elif distance == 2:
        clue = "🦴 Ancient bones buried shallowly."
    else:
        clue = "🌊 Just shells and sand."
    clues_found[island_index] = clue
    print(f"Survey results for {islands[island_index]}: {clue}")

def excavate(island_index):
    #Attempt a dig on an island
    global score

    if excavated[island_index]:
        print(f"You already excavated {islands[island_index]}. Nothing new.")
        return False

    excavated[island_index] = True

    if island_index == correct_island:
        print(f"🎉 You excavated {islands[island_index]} and discovered the ancient ruins!")
        score += 100
        return True
    else:
        #Random artifact finds
        finds = [
            ("🪨 Broken pottery shard", 5),
            ("🪓 Old stone tool", 10),
            ("🦴 Animal bones", 3),
            ("🌱 Charcoal from ancient fire", 7),
            ("❌ Nothing significant", 0)
        ]
        find, points = random.choice(finds)
        score += points
        print(f"Excavation at {islands[island_index]}: {find} (+{points} points)")
        return False

def show_map():
    #Show what we know so far
    print("\n📜 Current Expedition Notes:")
    for i, name in enumerate(islands):
        status = []
        if clues_found[i]:
            status.append(clues_found[i])
        if excavated[i]:
            status.append("⛏ Excavated")
        if not status:
            status.append("Unknown")
        print(f"- {name}: " + " | ".join(status))
    print(f"⭐ Current Score: {score}\n")

# --- Game Loop ---
while turns > 0:
    print(f"\nTurns remaining: {turns} | Score: {score}")
    action = input("Choose an action (survey, excavate, map, quit): ").lower()

    if action == "quit":
        print("Expedition ended early. The ruins remain hidden.")
        break
    elif action == "map":
        show_map()
        continue
    elif action in ["survey", "excavate"]:
        try:
            choice = int(input("Pick an island (1-5): ")) - 1
            if choice < 0 or choice > 4:
                print("Invalid island number.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        if action == "survey":
            survey(choice)
        elif action == "excavate" and excavate(choice):
                print(f"\n🏆 Final Score: {score}")
                break
    else:
        print("Invalid action. Try again.")
        continue

    turns -= 1

if turns == 0 and not excavated[correct_island]:
    print("\n⏳ You ran out of time! The ruins remain undiscovered...")
    print(f"Final Score: {score}")
