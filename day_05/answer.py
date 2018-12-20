# -*- coding: utf-8 -*-

import string

# --- part one ---


def parse_inputs(file):
    with open(file, 'r') as f:
        return f.readline().rstrip()


polymer = parse_inputs('input.txt')


def lower_upper():
    lower_upper = {}
    for letter in string.ascii_lowercase:
        lower_upper[letter.lower()] = letter.upper()
        lower_upper[letter.upper()] = letter.lower()
    return lower_upper


lower_upper = lower_upper()


def find_resulting_polymer(polymer):
    result = []
    for letter in polymer:
        if result and letter == lower_upper[result[-1]]:
            result.pop()
        else:
            result.append(letter)
    return result


print(f'The answer of part 1 is: {len(find_resulting_polymer(polymer))}')


# --- part two ---


def remove_letter(polymer, letter):
    return [l for l in polymer if l.lower() != letter]


def find_shortest_polymer(polymer):
    length_polymer = set()
    for letter in string.ascii_lowercase:
        altered_polymer = remove_letter(polymer, letter)
        length_polymer.add(len(find_resulting_polymer(altered_polymer)))
    return min(length_polymer)


print(f'The answer of part 2 is: {find_shortest_polymer(polymer)}')
