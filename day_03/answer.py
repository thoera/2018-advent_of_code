# -*- coding: utf-8 -*-

from collections import namedtuple
import numpy as np
import re

# --- part one ---

def get_coordinates(file):
    Coordinates = namedtuple('Coordinates', ['id', 'from_left', 'from_top',
                                             'width', 'height'])
    claims = []
    with open(file, 'r') as f:
        for claim in f:
            parsing = (
                    int(x)
                    for x in re.search(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)$',
                                       claim.rstrip())
                               .groups()
                    )
            claims.append(Coordinates(*(parsing)))
    return claims

claims = get_coordinates('input.txt')

def get_shape(claims):
    width = max([claim.from_left + claim.width for claim in claims])
    height = max([claim.from_top + claim.height for claim in claims])
    return (width, height)

def fill_matrix(shape, claims):
    matrix = np.zeros(shape)
    
    for claim in claims:
        matrix[claim.from_left:claim.from_left + claim.width,
               claim.from_top:claim.from_top + claim.height] += 1
    return matrix

result = fill_matrix(get_shape(claims), claims)

print(f'The answer of part 1 is: {np.sum(result > 1)}')

# --- part two ---

def find_claim_id(shape, claims):
    matrix = np.zeros(shape)
    throw_out = set()

    for claim in claims:
        matrix_subset = matrix[claim.from_left:claim.from_left + claim.width,
                               claim.from_top:claim.from_top + claim.height]
        if np.any(matrix_subset != 0):
            throw_out.update(np.unique(matrix_subset))
            throw_out.add(claim.id)
        matrix_subset += claim.id

    for claim in claims:
        if claim.id not in throw_out:
            return claim.id

claim_id = find_claim_id(get_shape(claims), claims)

print(f'The answer of part 2 is: {claim_id}')
