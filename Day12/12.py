def get_height(loc, height_map):
    x, y  = loc

    # if location out of bounds
    if x < 0 or y < 0 or x >= len(height_map[0]) or y >= len(height_map):
        return "~"

    height = height_map[y][x]

    # convert start and end
    if height == "S":
        return "a"
    elif height == "E":
        return "z"
    else:
        return height


def is_climable(cur_coord, new_coord, height_map):
    cur_height = get_height(cur_coord, height_map)
    new_height = get_height(new_coord, height_map)
    return ord(new_height) - ord(cur_height) < 2


def get_next_locations(height_map, cur_loc, visited):
    visit_next = []
    steps = [1, -1]
    cur_x, cur_y, path = cur_loc
    for step in steps:
        new_coords = [(cur_x, cur_y + step), (cur_x + step, cur_y)]
        for new_coord in new_coords:
            if new_coord in visited:
                continue
            if is_climable(cur_loc[0:2], new_coord, height_map):
                new_visited = path.copy()
                new_visited[cur_loc[0:2]] = get_height(cur_loc[0:2], height_map)
                visit_next.append((new_coord[0], new_coord[1], new_visited))
    return visit_next


def get_shortest_path(visit_order, height_map):
    visited = {}
    while visit_order:
        cur_loc = visit_order.pop(0)

        x, y = cur_loc[0:2]
        if height_map[y][x] == "E":
            return(len(cur_loc[2].keys()))

        if visited.get(cur_loc[0:2]):
            continue
        visited[cur_loc[0:2]] = 1
        visit_order += get_next_locations(height_map, cur_loc, visited)

    return 1000


def get_map_and_start():
    height_map = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if "S" in line:
                start = [(line.index("S"), i, {})]
            height_map.append(line)
    return height_map, start


def part_one():
    height_map, start = get_map_and_start()
    short_path = get_shortest_path(start, height_map)
    return short_path

print("Part 1: ", part_one())


"""
    Part 2
"""
def get_map_and_starts():
    height_map = []
    start_locations = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if "S" in line:
                start_locations.append((line.index("S"), i, {}))
            if "a" in line:
                start_locations.append((line.index("a"), i, {}))
            height_map.append(line)
    return height_map, start_locations


def part_two():
    height_map, start_locations = get_map_and_starts()
    shortest_path = 10000

    for start in start_locations:
        visit_order = [start]
        short_path = get_shortest_path(visit_order, height_map)
        if short_path < shortest_path:
            shortest_path = short_path

    return shortest_path

print("Part 2: ", part_two())
