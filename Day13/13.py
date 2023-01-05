def get_next_value(line, cur_index, level):
    # when ] new set
    print(line, cur_index, level)
    val = ""
    if cur_index >= len(line):
        return cur_index, val, level
    for i in range(cur_index, len(line), 1):
        char = line[i]
        if char == "[":
            level += 1
            val = "["
            return i + 1, val, level
        elif char == "]":
            level -= 1
            val = "]"
            return i + 1, val, level
        elif char == "," and val:
            return i + 1, val, level
        elif char.isnumeric():
            val += char


def part_one():
    ordered = []
    with open("test.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            pair1 = lines[i].strip()
            pair2 = lines[i + 1].strip()
            index1 = 0
            index2 = 0
            is_ordered = True
            level1, level2 = 0, 0
            val1 = 1
            while val1:
                index1, val1, level1 = get_next_value(pair1, index1, level1)
                index2, val2, level2 = get_next_value(pair2, index2, level2)
                print(index1, index2, val1, val2)
                if val1.isnumeric() and val2 == "[" and level1 > level2:
                    index2, val2, level2 = get_next_value(pair2, index2, level2)
                if val2.isnumeric() and val1 == "[" and level2 > level1:
                    index1, val1, level1 = get_next_value(pair1, index1, level1)
                if val1 != "" and val2 == "":
                    is_ordered = False
                    break
                if val1.isnumeric() and val2.isnumeric():
                    if int(val1) > int(val2):
                        print("INT")
                        is_ordered = False
                        break
                if val1 == "[" and val2 == "]" and level1 > level2:
                    print("LONG")
                    is_ordered = False
                    break
                if val1.isnumeric() and val2 == "]":
                    print("OVERFLOW")
                    is_ordered = False
                    break
            if is_ordered:
                ordered.append(i//3 + 1)

    return ordered

print("Part 1: ", part_one())
