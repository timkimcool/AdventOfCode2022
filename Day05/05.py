import queue

def create_queues(lines):
    input_array = []
    queues = {}

    # turn input into lists
    for line in lines:
        array = [line[i] for i in range(1, len(line), 4)]
        input_array.append(array)

    # create queues for each column
    queues = { int(num): queue.LifoQueue() for num in input_array[-1]}

    # populate queues
    for line in reversed(input_array[0:-1]):
        for i, val in enumerate(line):
            if val != " ":
                queues[i + 1].put(val)

    return queues


def read_moves(lines):
    """string to list of [count, from_bucket, to_bucket]"""
    moves = []
    for line in lines:
        line = line.split()
        move = [int(line[1]), int(line[3]), int(line[5])]
        moves.append(move)
    return moves


def process_moves1(moves, queues):
    for move in moves:
        count, from_bucket, to_bucket = move
        for _ in range(count):
            val = queues[from_bucket].get()
            queues[to_bucket].put(val)
    return queues


def part_one():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        # text to lifo queues
        queues = create_queues(lines[0:9])
        moves = read_moves(lines[10:])
        process_moves1(moves, queues)

        # get top values
        top_values = ""
        for queue in queues:
            top_values += queues[queue].get()

    return top_values

print("Part 1: ", part_one())


def process_moves2(moves, queues):
    for move in moves:
        count, from_bucket, to_bucket = move
        move_order = [queues[from_bucket].get() for _ in range(count)]
        for val in reversed(move_order):
            queues[to_bucket].put(val)
    return queues


def part_two():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        # text to lifo queues
        queues = create_queues(lines[0:9])
        moves = read_moves(lines[10:])
        process_moves2(moves, queues)

        # get top values
        top_values = ""
        for queue in queues:
            top_values += queues[queue].get()

    return top_values

print("Part 2: ", part_two())
