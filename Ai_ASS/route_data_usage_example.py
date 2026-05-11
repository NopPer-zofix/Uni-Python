from route_data_small import ROADS, LOCATIONS, DEFAULT_START, DEFAULT_GOAL

start_state = DEFAULT_START
goal_state = DEFAULT_GOAL

print(f"Start state: {start_state}")
print(f"Goal state: {goal_state}")
print()

print("Actions, outcomes and costs from Elm:")
for destination, distance in ROADS["Elm"]:
    print(f"Action: go({destination}), Outcome: {destination}, Cost: {distance}")

x, y = LOCATIONS["Elm"]
print()
print(f"(x, y) position of Elm: ({x}, {y})")
