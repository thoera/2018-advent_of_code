# -*- coding: utf-8 -*-

import re


# --- part one ---


def parse_inputs(file):
    s = re.compile(
        "position=<(.*[0-9]+), (.*[0-9]+)> velocity=<(.*[0-9]+), (.*[0-9]+)>"
    )
    position_velocity = []
    with open(file, "r") as f:
        for line in f:
            parsing = re.search(s, line).groups()
            position = [int(parsing[0]), int(parsing[1])]
            velocity = [int(parsing[2]), int(parsing[3])]
            position_velocity.append([position, velocity])
    return position_velocity


positions = parse_inputs("input.txt")


def compute_positions(positions):
    return [
        [[sum(x) for x in zip(position[0], position[1])], position[1]]
        for position in positions
    ]


def min_max_x_y(positions):
    x, y = zip(*[i[0] for i in positions])
    return min(x), min(y), max(x), max(y)


def print_message(positions, min_x, min_y, max_x, max_y):
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if [j, i] in [position for position, velocity in positions]:
                print("#", end="")
            else:
                print(".", end="")
        print("")


time = 0
while True:
    min_x_init, min_y_init, max_x_init, max_y_init = min_max_x_y(positions)

    new_positions = compute_positions(positions)
    min_x, min_y, max_x, max_y = min_max_x_y(new_positions)

    if max_x > max_x_init and max_y > max_y_init:
        print_message(
            positions, min_x_init, min_y_init, max_x_init, max_y_init
        )
        break
    else:
        positions = new_positions
        time += 1


# --- part two ---


print(f"The answer of part 2 is: {time}")
