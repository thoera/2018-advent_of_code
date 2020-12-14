# -*- coding: utf-8 -*-


# --- part one ---


def parse_inputs(file):
    with open(file, "r") as f:
        inputs = f.readlines()
        state = inputs[0].rstrip().split("initial state: ")[1]
        rules = [line.rstrip() for line in inputs[2:]]
        return state, rules


state, rules = parse_inputs("input.txt")
rules = {r[0]: r[1] for r in [rule.split(" => ") for rule in rules]}


def spread_plant_nearby(state, rules, origin):
    state = f".....{state}....."
    origin += -3  # -5 for the dots and +2 because we loop from the 3rd element

    new_state = []
    for position in range(2, len(state) - 2):
        rule = state[position - 2 : position + 3]
        spread = rules[rule]
        new_state.append(spread)

    while new_state[0] == ".":
        new_state.pop(0)
        origin += 1
    while new_state[-1] == ".":
        new_state.pop()

    return "".join(new_state), origin


def sum_position(state, origin):
    return sum(idx + origin for idx, plot in enumerate(state) if plot == "#")


origin = 0
for generation in range(1, 21):
    state, origin = spread_plant_nearby(state, rules=rules, origin=origin)

print(f"The answer of part 1 is: {sum_position(state, origin)}")


# --- part two ---


state, rules = parse_inputs("input.txt")
rules = {r[0]: r[1] for r in [rule.split(" => ") for rule in rules]}

N = 50_000_000_000
origin = 0
previous_filled_pots = 0

for generation in range(1, N):
    new_state, origin = spread_plant_nearby(state, rules=rules, origin=origin)
    filled_pots = sum_position(new_state, origin)
    delta = filled_pots - previous_filled_pots
    if new_state == state:
        break
    state = new_state
    previous_filled_pots = filled_pots

result = (N - generation) * delta + filled_pots
print(f"The answer of part 2 is: {result}")
