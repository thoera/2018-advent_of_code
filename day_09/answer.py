# -*- coding: utf-8 -*-

from collections import defaultdict
from itertools import cycle
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
    idx = 0
    game = [0]

    for marble in range(1, last_marble + 1):
        player = next(players)
        len_ = len(game)
        if marble % 23 == 0:
            if idx >= 7:
                idx -= 7
            else:
                idx = len_ + idx - 7
            players_score[marble % players] += marble + game.pop(idx)
        else:
            idx += 2
            if idx > len_:
                idx -= len_
            game.insert(idx, marble)
    return game, players_score


game, players_score = compute_game(players, last_marble)
print(f'The answer of part 1 is: {max(players_score.values())}')


# --- part two ---

game, players_score = compute_game(players, last_marble * 100)
print(f'The answer of part 2 is: {max(players_score.values())}')
