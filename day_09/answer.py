# -*- coding: utf-8 -*-

from collections import defaultdict, deque
import re


# --- part one ---


def parse_inputs(file):
    with open(file) as f:
        inputs = f.read()
    s = re.compile('(^[0-9]+) players.+?([0-9]+) points$')
    players, last_marble = re.search(s, inputs).groups()
    return int(players), int(last_marble)


players, last_marble = parse_inputs('input.txt')


def compute_game(players, last_marble):
    players_score = defaultdict(int)
    game = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            game.rotate(7)
            players_score[marble % players] += marble + game.pop()
            game.rotate(-1)
        else:
            game.rotate(-1)
            game.append(marble)
    return game, players_score


game, players_score = compute_game(players, last_marble)
print(f'The answer of part 1 is: {max(players_score.values())}')


# --- part two ---


game, players_score = compute_game(players, last_marble * 100)
print(f'The answer of part 2 is: {max(players_score.values())}')
