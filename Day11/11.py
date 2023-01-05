def process_input(lines):
    monkey = {}

    monkey["name"] = lines[0].strip()

    items = lines[1].strip()
    monkey["items"] = [int(x) for x in items[items.index(": ") + 2:].split(", ")]

    op = lines[2].strip()
    monkey["op"] = lambda old: eval(op[op.index("= ") + 2:])

    test = lines[3].strip()
    monkey["test"] = int(test[test.index("by ") + 3:])

    true = lines[4].strip()
    monkey["true"] = int(true[true.index("monkey ") + 6:])

    false = lines[5].strip()
    monkey["false"] = int(false[false.index("monkey ") + 6:])

    monkey["count"] = 0
    return monkey


def get_monkeys():
    monkeys = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 7):
            monkey = process_input(lines[i:i+6])
            monkeys.append(monkey)
    return monkeys


def handle_item(monkey, monkeys):
    while monkey["items"]:
        item = monkey["items"].pop(0)
        monkey["count"] += 1
        worry = monkey["op"](item)
        worry = worry // 3
        truth = "true" if (worry % monkey["test"] == 0) else "false"
        monkeys[monkey[truth]]["items"].append(worry)

def part_one():
    monkeys = get_monkeys()
    for _ in range(20):
        for monkey in monkeys:
            handle_item(monkey, monkeys)
    counts = [monkey["count"] for monkey in monkeys]
    counts.sort()
    return counts[-1] * counts[-2]

print("Part 1: ", part_one())


"""
    Part 2
"""
from functools import reduce
def handle_item2(monkey, monkeys, chinese_remainder):
    while monkey["items"]:
        item = monkey["items"].pop(0)
        monkey["count"] += 1
        worry = monkey["op"](item)
        worry %= chinese_remainder
        truth = "true" if (worry % monkey["test"] == 0) else "false"
        monkeys[monkey[truth]]["items"].append(worry)

def part_two():
    monkeys = get_monkeys()
    chinese_remainder = reduce(lambda x, y: x * y, [monkey["test"] for monkey in monkeys], 1)
    for _ in range(10000):
        for monkey in monkeys:
            handle_item2(monkey, monkeys, chinese_remainder)
    counts = [monkey["count"] for monkey in monkeys]
    counts.sort()
    return counts[-1] * counts[-2]

print("Part 2: ", part_two())
