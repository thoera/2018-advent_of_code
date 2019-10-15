# -*- coding: utf-8 -*-

from collections import Counter


# --- part one ---


def parse_inputs(file):
    with open(file, 'r') as f:
        return [line.rstrip() for line in f]


inputs = parse_inputs('input.txt')


def compute_checksum(inputs):
    two_times = 0
    three_times = 0

    for ID in inputs:
        counter = Counter(ID)
        if 2 in counter.values():
            two_times += 1
        if 3 in counter.values():
            three_times += 1
    return two_times * three_times


print(f'The answer of part 1 is: {compute_checksum(inputs)}')


# --- part two ---


def find_boxes(inputs):
    for string_1 in inputs:
        for string_2 in inputs:
            common_letters = [i for i, j in zip(string_1, string_2) if i == j]
            if len(common_letters) == len(string_1) - 1:
                return ''.join(common_letters)


print(f'The answer of part 2 is: {find_boxes(inputs)}')
