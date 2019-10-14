# -*- coding: utf-8 -*-

import numpy as np
from scipy.spatial import distance


# --- part one ---


def parse_inputs(file):
    return np.genfromtxt(file, dtype='int', delimiter=',')


inputs = parse_inputs('input.txt')


def create_grid(inputs, padding=0):
    max_coord = np.max(inputs, axis=0)
    xx, yy = np.meshgrid(range(0 - padding, max_coord[0] + 1 + padding),
                         range(0 - padding, max_coord[1] + 1 + padding))
    return np.dstack([xx, yy]).reshape(-1, 2)


grid_coord = create_grid(inputs, padding=0)


def compute_manathan_distances(inputs, grid_coord):
    return distance.cdist(inputs, grid_coord, metric='cityblock')


distances = compute_manathan_distances(inputs, grid_coord)


def compute_areas(distances, grid_coord):
    min_distances = np.min(distances, axis=0)
    idx_arr = (min_distances[np.newaxis, :] == distances)

    # remove non-unique minima
    idx_unique = (np.sum(idx_arr, axis=0) == 1)
    idx_arr = idx_arr[:, idx_unique]

    # keep only the valid points (those not on the border of the grid)
    border = np.logical_or(
            np.logical_or(grid_coord[:, 0] == np.min(grid_coord[:, 0]),
                          grid_coord[:, 0] == np.max(grid_coord[:, 0])),
            np.logical_or(grid_coord[:, 1] == np.min(grid_coord[:, 1]),
                          grid_coord[:, 1] == np.max(grid_coord[:, 1]))
            )

    valid_points = np.invert(np.any(idx_arr[:, border[idx_unique]], axis=1))

    # return the area for each input
    return np.sum(idx_arr[valid_points, :], axis=1)


areas = compute_areas(distances, grid_coord)


def compute_max_area(areas):
    return np.max(areas)


print(f'The answer of part 1 is: {compute_max_area(areas)}')


# --- part two ---


def compute_largest_region(distances, within):
    return np.sum(np.sum(distances, axis=0) < within)


print(f'The answer of part 2 is: {compute_largest_region(distances, 10000)}')
