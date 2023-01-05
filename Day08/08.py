def is_visible(start_x, start_y, grid, val):
    visible = True
    for i in range(1, len(grid[0]) - start_x, 1):
        new_val = grid[start_y][start_x + i]
        if new_val >= val:
            visible = False
            break
    if visible:
        return True

    visible = True
    for i in range(0, start_x, 1):
        new_val = grid[start_y][start_x - i - 1]
        if new_val >= val:
            visible = False
            break
    if visible:
        return True

    visible = True
    for i in range(1, len(grid) - start_y, 1):
        new_val = grid[start_y + i][start_x]
        if new_val >= val:
            visible = False
            break
    if visible:
        return True

    visible = True
    for i in range(0, start_y, 1):
        new_val = grid[start_y - i - 1][start_x]
        if new_val >= val:
            visible = False
            break
    if visible:
        return True

    return False

def part_one():
    grid = []
    count = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            grid.append([int(x) for x in line.strip()])
            
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if is_visible(x, y, grid, val):
                count += 1

    return count

print("Part 1: ", part_one())


from functools import reduce
def get_scenic_score(start_x, start_y, grid, val):
    score = []

    count = 0
    for i in range(1, len(grid[0]) - start_x, 1):
        new_val = grid[start_y][start_x + i]
        count += 1
        if new_val >= val:
            break
    score.append(count)

    count = 0
    for i in range(0, start_x, 1):
        new_val = grid[start_y][start_x - i - 1]
        count += 1
        if new_val >= val:
            break
    score.append(count)

    count = 0
    for i in range(1, len(grid) - start_y, 1):
        new_val = grid[start_y + i][start_x]
        count += 1
        if new_val >= val:
            break
    score.append(count)

    count = 0
    for i in range(0, start_y, 1):
        new_val = grid[start_y - i - 1][start_x]
        count += 1
        if new_val >= val:
            break
    score.append(count)

    score = reduce(lambda x, y: x * y, score, 1)
    return score


"""
    Part 2
"""
def part_two():
    grid = []
    max_score = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            grid.append([int(x) for x in line.strip()])
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            score = get_scenic_score(x, y, grid, val)
            max_score = max(max_score, score)

    return max_score

print("Part 2: ", part_two())
