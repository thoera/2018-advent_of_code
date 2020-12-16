# -*- coding: utf-8 -*-

from collections import Counter
from operator import itemgetter

# --- part one ---


def parse_inputs(file):
    with open(file) as f:
        return [[m for m in line.rstrip()] for line in f]


def build_full_tracks(tracks):
    full_tracks = [track[:] for track in tracks]
    for col, track in enumerate(full_tracks):
        for row, piece_of_track in enumerate(track):
            if piece_of_track in ["<", ">"]:
                full_tracks[col][row] = "-"
            if piece_of_track in ["^", "v"]:
                full_tracks[col][row] = "|"
    return full_tracks


def find_carts(tracks):
    carts = []
    for col, track in enumerate(tracks):
        for row, piece_of_track in enumerate(track):
            if piece_of_track in ["<", ">", "v", "^"]:
                carts.append(
                    {
                        "x": row,
                        "y": col,
                        "direction": piece_of_track,
                        "state": "<",
                    }
                )
    return carts


def order_carts(carts):
    return carts.sort(key=itemgetter("y", "x"))


def get_next_piece_of_track(tracks, x, y, direction):
    if direction == "<":
        move = (-1, 0)
    if direction == ">":
        move = (1, 0)
    if direction == "^":
        move = (0, -1)
    if direction == "v":
        move = (0, 1)

    return tracks[y + move[1]][x + move[0]]


def direction_at_intersection(direction, state):
    if direction == "<":
        if state == "<":
            new_direction = "v"
        if state == "|":
            new_direction = "<"
        if state == ">":
            new_direction = "^"
    if direction == ">":
        if state == "<":
            new_direction = "^"
        if state == "|":
            new_direction = ">"
        if state == ">":
            new_direction = "v"
    if direction == "^":
        if state == "<":
            new_direction = "<"
        if state == "|":
            new_direction = "^"
        if state == ">":
            new_direction = ">"
    if direction == "v":
        if state == "<":
            new_direction = ">"
        if state == "|":
            new_direction = "v"
        if state == ">":
            new_direction = "<"

    return new_direction


def update_state(state):
    if state == "<":
        return "|"
    if state == "|":
        return ">"
    if state == ">":
        return "<"


def get_new_direction(piece_of_track, direction, state):
    if piece_of_track == "-" or piece_of_track == "|":
        new_direction = direction
    if piece_of_track == "+":
        new_direction = direction_at_intersection(direction, state)
        state = update_state(state)
    if piece_of_track == "/":
        if direction == "<":
            new_direction = "v"
        if direction == ">":
            new_direction = "^"
        if direction == "^":
            new_direction = ">"
        if direction == "v":
            new_direction = "<"
    if piece_of_track == "\\":
        if direction == "<":
            new_direction = "^"
        if direction == ">":
            new_direction = "v"
        if direction == "^":
            new_direction = "<"
        if direction == "v":
            new_direction = ">"

    return new_direction, state


def update_coordinates(x, y, direction):
    if direction == "<":
        update = (-1, 0)
    if direction == ">":
        update = (1, 0)
    if direction == "^":
        update = (0, -1)
    if direction == "v":
        update = (0, 1)

    return x + update[0], y + update[1]


def move_cart(tracks, cart):
    x, y = cart["x"], cart["y"]
    cart["x"], cart["y"] = update_coordinates(
        x, y, cart["direction"]
    )
    piece_of_track = get_next_piece_of_track(
        tracks, x, y, cart["direction"]
    )
    cart["direction"], cart["state"] = get_new_direction(
        piece_of_track, cart["direction"], cart["state"]
    )
    return cart


def update_tracks(tracks, carts):
    tracks_updated = [track[:] for track in tracks]
    for cart in carts:
        tracks_updated[cart["y"]][cart["x"]] = cart["direction"]
    return tracks_updated


def is_crash(carts):
    counts = Counter((cart["x"], cart["y"]) for cart in carts)
    for item, value in counts.items():
        if value > 1:
            return item


def find_first_crash(file, show=False):
    tracks = parse_inputs(file)
    full_tracks = build_full_tracks(tracks=tracks)
    carts = find_carts(tracks=tracks)

    if show:
        print("Tracks:\n")
        for track in tracks:
            print("".join(track))
        print("\nCarts:\n")
        print(f"{carts}\n")

    order_carts(carts)

    while True:
        for cart in carts:
            cart = move_cart(tracks=full_tracks, cart=cart)
            crash = is_crash(carts=carts)
            if crash:
                print(f"There is a CRASH at {crash}!\n")
                break
        else:
            tracks = update_tracks(tracks=full_tracks, carts=carts)
            if show:
                for track in tracks:
                    print("".join(track))
                print("\n")
            continue
        break


find_first_crash("input.txt")


# --- part two ---


def remove_crashed_carts(carts, crash):
    return [cart for cart in carts
            if cart["x"] != crash[0] or cart["y"] != crash[1]]


def find_last_cart(file, show=False):
    tracks = parse_inputs(file)
    full_tracks = build_full_tracks(tracks=tracks)
    carts = find_carts(tracks=tracks)

    if show:
        print("Tracks:\n")
        for track in tracks:
            print("".join(track))
        print("\nCarts:\n")
        print(f"{carts}\n")

    order_carts(carts)

    while len(carts) > 1:
        for cart in carts:
            cart = move_cart(tracks=full_tracks, cart=cart)
            crash = is_crash(carts=carts)
            if crash:
                print(f"There is a CRASH at {crash}!\n")
                carts = remove_crashed_carts(carts=carts, crash=crash)
        else:
            tracks = update_tracks(tracks=full_tracks, carts=carts)
            if show:
                for track in tracks:
                    print("".join(track))
                print("\n")
            continue
    try:
        location = (carts[0]["x"], carts[0]["y"])
        print(f"Coordinates of the last remaining cart: {location}")
    except IndexError:
        print("There is no more cart on the tracks!")
        pass


find_last_cart("input.txt")
