def head_step(x, y, dir):
    if dir == "R":
        return x + 1, y
    if dir == "L":
        return x - 1, y
    if dir == "U":
        return x, y + 1
    else:
        return x, y - 1


def tail_step(head_x, head_y, tail_x, tail_y):
    x_diff, y_diff = 0, 0
    diag = (abs(head_y - tail_y) + abs(head_x - tail_x)) > 2
    if abs(head_x - tail_x) > 1 or diag:
        x_diff = 1 if head_x > tail_x else -1
    if abs(head_y - tail_y) > 1 or diag:
        y_diff = 1 if head_y > tail_y else -1
    return tail_x + x_diff, tail_y + y_diff


def part_one():
    visited = {}
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            dir, steps = line.strip().split()
            for _ in range(int(steps)):
                head_x, head_y = head_step(head_x, head_y, dir)
                tail_x, tail_y = tail_step(head_x, head_y, tail_x, tail_y)
                coord = f"{tail_x},{tail_y}"
                visited[coord] = 1
    return len(visited.keys())

print("Part 1: ", part_one())


"""
    Part 2
"""
def part_two():
    visited = {}
    head_x, head_y = 0, 0
    tails = [[0,0] for _ in range(9)]
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            dir, steps = line.strip().split()
            for _ in range(int(steps)):
                head_x, head_y = head_step(head_x, head_y, dir)
                for i, tail in enumerate(tails):
                    tail_x, tail_y = (head_x, head_y) if (i == 0) else tails[i-1]
                    tails[i] = tail_step(tail_x, tail_y, tail[0], tail[1])
                coord = f"{tails[-1][0]},{tails[-1][1]}"
                visited[coord] = 1
    return len(visited.keys())

print("Part 2: ", part_two())
