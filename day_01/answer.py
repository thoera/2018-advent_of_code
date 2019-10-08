# -*- coding: utf-8 -*-

from itertools import cycle


# --- part one ---


def parse_inputs(file):
    with open(file, 'r') as f:
        return [int(line) for line in f]

inputs = parse_inputs('input.txt')


def compute_frequency(inputs):
    return sum(inputs)

print(f'The answer of part 1 is: {compute_frequency(inputs)}')


# --- part two ---


def compute_calibrated_frequency(inputs):
    frequency = 0
    previous_frequencies = {frequency}

    for i in cycle(inputs):
        frequency += i
        if frequency in previous_frequencies:
            return frequency
        else:
            previous_frequencies.add(frequency)

print(f'The answer of part 2 is: {compute_calibrated_frequency(inputs)}')
