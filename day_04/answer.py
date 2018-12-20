# -*- coding: utf-8 -*-

from collections import namedtuple
import numpy as np
import re


# --- part one ---


def load_inputs(file):
    with open(file, 'r') as f:
        return sorted([line.rstrip() for line in f])


inputs = load_inputs('input.txt')


def parse_inputs(inputs):
    Input = namedtuple('Input', ['timestamp', 'guard_id', 'action'])

    timeline = []
    guards_id = set()
    for i in inputs:
        if 'Guard' in i:
            parsing = re.compile(r'\[(.*)\] Guard #(\d*) ([ \w]*)')
            timestamp, guard_id, action = parsing.search(i).groups()
            guards_id.add(guard_id)
        else:
            parsing = re.compile(r'\[(.*)\] ([ \w]*)')
            timestamp, action = parsing.search(i).groups()
        timeline.append(Input(timestamp, guard_id, action))
    return timeline, guards_id


records, guards_id = parse_inputs(inputs)
guards_id = {guard_id: index for index, guard_id in enumerate(guards_id)}


def fill_timeline(timeline, records):
    for record in records:
        if record.action == 'falls asleep':
            start = int(record.timestamp[-2:])
        elif record.action == 'wakes up':
            end = int(record.timestamp[-2:])
            timeline[guards_id[record.guard_id], start:end + 1] += 1
    return timeline


timeline = fill_timeline(
        timeline=np.zeros((len(guards_id), 60), dtype=np.int8),
        records=records
        )


def find_sloppy_guard(timeline, guards_id=guards_id):
    guard = np.sum(timeline, axis=1).argmax()
    return list(guards_id.keys())[list(guards_id.values()).index(guard)]


sloppy_guard = find_sloppy_guard(timeline)


def find_minute(timeline, sloppy_guard, guards_id=guards_id):
    return np.argmax(timeline[guards_id[sloppy_guard], :])


minute = find_minute(timeline, sloppy_guard)

print(f'The answer of part 1 is: {int(sloppy_guard) * minute}')


# --- part two ---


def find_sloppy_guard_2(timeline, guards_id=guards_id):
    result = np.unravel_index(np.argmax(timeline), timeline.shape)
    guard = list(guards_id.keys())[list(guards_id.values()).index(result[0])]
    return (guard, result[1])


sloppy_guard_2 = find_sloppy_guard_2(timeline, guards_id=guards_id)

print(f'The answer of part 2 is: {int(sloppy_guard_2[0]) * sloppy_guard_2[1]}')
