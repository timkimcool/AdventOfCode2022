def calculate_score(file, scoring):
    score = 0
    for line in file.readlines():
        opp, me = line.strip().split(" ")
        score += scoring[opp][me] + scoring[me]
    return score


def part_one():
    with open("input.txt", "r") as file:
        scoring = {
            "A": { "X": 3, "Y": 6, "Z": 0 },
            "B": { "X": 0, "Y": 3, "Z": 6 },
            "C": { "X": 6, "Y": 0, "Z": 3 },
            "X": 1, "Y": 2, "Z": 3,
        }
        score = calculate_score(file, scoring)
    return score

print("Part 1: ", part_one())


def part_two():
    with open("input.txt", "r") as file:
        scoring = {
            "A": { "X": 3, "Y": 1, "Z": 2 },
            "B": { "X": 1, "Y": 2, "Z": 3 },
            "C": { "X": 2, "Y": 3, "Z": 1 },
            "X": 0, "Y": 3, "Z": 6,
        }
        score = calculate_score(file, scoring)
    return score

print("Part 2: ", part_two())
