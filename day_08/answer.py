# -*- coding: utf-8 -*-


# --- part one ---


def parse_inputs(file):
    with open(file, 'r') as f:
        return [int(item) for item in f.read().split()]


inputs = parse_inputs('input.txt')


def get_metadata(inputs):
    idx = 0
    metadata = []
    while inputs:
        if inputs[idx] == 0:
            nb_metadata = inputs[idx + 1]
            metadata.extend(inputs[(idx + 2):(idx + 2 + nb_metadata)])
            inputs = inputs[:idx] + inputs[(idx + 2 + nb_metadata):]
            if inputs:
                inputs[idx - 2] += -1
            idx -= 2
        else:
            idx += 2
    return metadata


print(f'The answer of part 1 is: {sum(get_metadata(inputs))}')


# --- part two ---


inputs = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
print(f'The answer of part 2 is: {}')
