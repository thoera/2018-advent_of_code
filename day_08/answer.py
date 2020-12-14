# -*- coding: utf-8 -*-


# --- part one ---


def parse_inputs(file):
    with open(file, "r") as f:
        return [int(item) for item in f.read().split()]


inputs = parse_inputs("input.txt")


def compute_value(inputs):
    children, metadata = inputs[:2]
    inputs = inputs[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, inputs = compute_value(inputs)
        totals += total
        scores.append(score)

    totals += sum(inputs[:metadata])

    if children == 0:
        return (totals, sum(inputs[:metadata]), inputs[metadata:])
    else:
        return (
            totals,
            sum(
                scores[k - 1]
                for k in inputs[:metadata]
                if k > 0 and k <= len(scores)
            ),
            inputs[metadata:],
        )


total, value, remaining = compute_value(inputs)


print(f"The answer of part 1 is: {total}")


# --- part two ---


print(f"The answer of part 2 is: {value}")
