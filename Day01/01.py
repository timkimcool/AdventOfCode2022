def part_one():
    with open("input.txt", "r") as file:
        max = 0
        current_sum = 0
        for line in file.readlines():
            if line != "\n":
                current_sum += int(line)
            else:
                if current_sum > max:
                    max = current_sum
                current_sum = 0
    return max

print("Part 1: ", part_one())


def part_two():
    with open("input.txt", "r") as file:
        calories = []
        current_sum = 0
        for line in file.readlines():
            if line != "\n":
                current_sum += int(line)
            else:
                calories.append(current_sum)
                current_sum = 0
        calories.sort(reverse=True)
    return sum(calories[0:3])
print("Part 2: ", part_two())
