def change_directory(input, directory_list, file_system):
    if input == "/":
        return [file_system]
    elif input == "..":
        directory_list.pop()
        return directory_list
    else:
        directory = directory_list[-1]
        directory[input] = directory.get(input, {})
        directory_list.append(directory[input])
        return directory_list


def ls(val1, val2, directory_list):
    directory = directory_list[-1]
    if val1 == "dir":
        directory[val2] = directory.get(val2, {})
    else:
        directory[val2] = val1


def create_file_system(lines):
    # input to dictionary
    file_system = {}
    directory_list = []
    for line in lines:
        vals = line.split()
        if vals[0] == "$":
            if vals[1] == "cd":
                directory_list = change_directory(vals[2], directory_list, file_system)
        else:
            ls(vals[0], vals[1], directory_list)
    return file_system


def get_size(directory, sizes):
    # recursive function to get size of directories
    total = 0
    for value in directory.values():
        total += get_size(value, sizes) if isinstance(value, dict) else int(value)
    sizes.append(total)
    return total

def part_one():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        # create a dictionary representation of the file system
        file_system = create_file_system(lines)

        # get all the sizes of directories
        sizes = []
        get_size(file_system, sizes)

        total = 0
        for size in sizes:
            if size <= 100000:
                total += size
    return total

print("Part 1: ", part_one())


def part_two():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        # create a dictionary representation of the file system
        file_system = create_file_system(lines)

        # get all the sizes of directories
        sizes = []
        get_size(file_system, sizes)

        # sort largest, to smallest
        sizes.sort(reverse=True)
        TOTAL_SPACE = 70000000
        UPDATE_SIZE = 30000000
        current_used_space = sizes[0]
        current_available_space = TOTAL_SPACE - current_used_space
        needed_space = UPDATE_SIZE - current_available_space
        previous_value = 0
        for size in sizes:
            if size >= needed_space:
                previous_value = size
            else:
                return previous_value

print("Part 2: ", part_two())
