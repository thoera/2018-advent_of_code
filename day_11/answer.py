# -*- coding: utf-8 -*-

import numpy as np
import re


# --- part one ---


def parse_input(file):
    with open(file) as f:
        return int(re.findall(r'\d+', f.read())[0])


serial_number = parse_input('input.txt')


def compute_power(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    fuel_cell = (power_level + serial_number) * rack_id
    fuel_cell = (fuel_cell // 100) % 10
    fuel_cell -= 5
    return fuel_cell


def compute_grid(shape, serial_number):
    grid = np.empty(shape, dtype='int')

    nrow, ncol = shape
    for row in range(nrow):
        for col in range(ncol):
            grid[row, col] = compute_power(row + 1, col + 1, serial_number)
    return grid


grid = compute_grid(shape=(300, 300), serial_number=serial_number)


def compute_power_window(grid, window=(3, 3)):
    nrow, ncol = grid.shape
    submatrices = []
    for row in range(nrow - window[0] + 1):
        for col in range(ncol - window[1] + 1):
            submatrices.append(grid[row:row + window[0], col:col + window[1]])
    return submatrices


submatrices = compute_power_window(grid)


def find_idx(submatrices, shape=(300, 300), window=(3, 3)):
    nrow, ncol = shape
    argmax_ = np.argmax([np.sum(submatrix) for submatrix in submatrices])
    return (argmax_ // (nrow - window[0] + 1) + 1,
            argmax_ % (ncol - window[1] + 1) + 1)


print(f'The answer of part 1 is: {find_idx(submatrices)}')


# --- part two ---


def compute_max_power_window(submatrices, shape=(300, 300), window=(3, 3)):
    nrow, ncol = shape
    return np.max([np.sum(submatrix) for submatrix in submatrices])


def compute_power_window_range(grid, range_window=(1, 300)):
    max_window = {}
    for size in range(range_window[0], range_window[1] + 1):
        submatrices = compute_power_window(grid, window=(size, size))
        max_window[size] = (compute_max_power_window(submatrices,
                                                     window=(size, size)),
                            (find_idx(submatrices, window=(size, size))))
    return max_window


max_window = compute_power_window_range(grid, range_window=(1, 300))
max_size = max(max_window, key=lambda key: max_window[key][0])

print(f'The answer of part 2 is: {max_window[max_size][1], max_size}')
