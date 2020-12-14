# -*- coding: utf-8 -*-

import networkx as nx


# --- part one ---


def parse_inputs(file):
    with open(file, "r") as f:
        return [(line[5], line[-13]) for line in f]


inputs = parse_inputs("input.txt")


def compute_topological_sort(inputs):
    return "".join(nx.lexicographical_topological_sort(nx.DiGraph(inputs)))


print(f"The answer of part 1 is: {compute_topological_sort(inputs)}")


# --- part two ---


def compute_time(inputs):
    graph = nx.DiGraph(inputs)
    task_times = []
    tasks = []
    time = 0
    while task_times or graph:
        available_tasks = [
            t for t in graph if t not in tasks and graph.in_degree(t) == 0
        ]
        if available_tasks and len(task_times) < 5:
            task = min(available_tasks)
            task_times.append(ord(task) - 4)
            tasks.append(task)
        else:
            min_time = min(task_times)
            completed = [
                tasks[i] for i, v in enumerate(task_times) if v == min_time
            ]
            task_times = [v - min_time for v in task_times if v > min_time]
            tasks = [t for t in tasks if t not in completed]
            time += min_time
            graph.remove_nodes_from(completed)
    return time


print(f"The answer of part 2 is: {compute_time(inputs)}")
