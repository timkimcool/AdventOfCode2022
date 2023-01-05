def increment_cycle(cycle, total, special_cycle, x):
    cycle += 1
    if cycle in special_cycle:
        total += cycle * x
    return cycle, total

def part_one():
    special_cycle = [cycle for cycle in range(20, 221, 40)]
    x = 1
    total = 0
    cycle = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            inst, _, count = line.strip().partition(" ")
            cycle, total = increment_cycle(cycle, total, special_cycle, x)
            if inst == "addx":
                cycle, total = increment_cycle(cycle, total, special_cycle, x)
                x += int(count)
    return total

print("Part 1: ", part_one())


"""
    Part 2
"""
def write_pixel(output, cycle, x):
    output += "#" if x <= cycle <= x+2 else "."
    cycle += 1
    if cycle > 39:
        output += "\n"
        cycle = 0
    return output, cycle


def part_two():
    output = "\n"
    x, cycle = 0, 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            inst, _, count = line.strip().partition(" ")
            output, cycle = write_pixel(output, cycle, x)
            if inst == "addx":
                output, cycle = write_pixel(output, cycle, x)
                x += int(count)
    return output

print("Part 2: ", part_two())
