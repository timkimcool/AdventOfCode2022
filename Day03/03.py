def get_priority(items):
    sum = 0
    for char in items:
        subtract = ord("a") - 1 if char.islower() else ord("A") - 27
        sum += ord(char) - subtract
    return sum


def get_common_items(file):
    shared = []
    for line in file.readlines():
        items = {}
        mid = len(line)//2
        for char in line[:mid]:
            items[char] = True
        for char in line[mid:]:
            if char in items:
                shared.append(char)
                break


def part_one():
    with open("input.txt", "r") as file:
        shared = get_common_items(file)
        sum  = get_priority(shared)

    return sum

print("Part 1: ", part_one())


def part_two():
    with open("input.txt", "r") as file:
        badge = []
        counter = 0
        # get common items
        for line in file.readlines():
            counter += 1
            if counter == 1:
                items = {}
                for char in line:
                    items[char] = 1
            else:
                for char in line:
                    if items.get(char, 0) == (counter - 1):
                        items[char] = counter
                    if items.get(char, 0) == 3:
                        badge.append(char)
                        counter = 0
                        break
        # calculate priority
        sum = get_priority(badge)

    return sum

print("Part 2: ", part_two())
