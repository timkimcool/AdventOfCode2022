def part_one():
    with open("input.txt", "r") as file:
        pairs = 0
        for line in file.readlines():
            elf1, elf2 = line.strip().split(",")
            elf1 = [int(x) for x in elf1.split("-")]
            elf2 = [int(x) for x in elf2.split("-")]
            if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
                pairs += 1
    return pairs

print("Part 1: ", part_one())


def part_two():
    with open("input.txt", "r") as file:
        pairs = 0
        for line in file.readlines():
            elf1, elf2 = line.strip().split(",")
            elf1 = [int(x) for x in elf1.split("-")]
            elf2 = [int(x) for x in elf2.split("-")]
            if elf1[0] <= elf2[0] <= elf1[1] or elf2[0] <= elf1[0] <= elf2[1]:
                pairs += 1
    return pairs

print("Part 2: ", part_two())
