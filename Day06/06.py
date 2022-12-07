import queue

def process_message(size, msg):
    marker_queue = queue.Queue(size)
    for i, char in enumerate(msg):
        if marker_queue.qsize() == size:
            marker_queue.get()
        marker_queue.put(char)
        if len(set(marker_queue.queue)) == size:
            return i + 1

def part_one():
    with open("input.txt", "r") as file:
        msg = file.readlines()[0]
        return process_message(4, msg)

print("Part 1: ", part_one())


def part_two():
    with open("input.txt", "r") as file:
        msg = file.readlines()[0]
        return process_message(14, msg)

print("Part 2: ", part_two())
