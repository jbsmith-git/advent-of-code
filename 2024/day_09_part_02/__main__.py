def import_input() -> list[int]:

    with open("input.txt", "r") as input_file:
        line = input_file.readlines()[0]

    disk_map = [int(i) for i in line.replace("\n", "")]

    return disk_map


def expand_disk_map(disk_map: list[int]) -> list[int, str]:

    expanded_disk_map = []
    for i, value in enumerate(disk_map):

        if i % 2 == 1:
            expanded_disk_map.extend(list("." * value))
        else:
            expanded_disk_map.extend([i // 2 for d in range(value)])

    return expanded_disk_map


def compact_hard_drive(disk_map: list[int, str]) -> list[int, str]:

    ## Compute the space map of the disk {(index, length), ...}
    space_map = set()
    space_start = None
    i = 0
    while i < len(disk_map):
        if disk_map[i] != ".":
            if space_start:
                space_map.add((space_start, i - space_start))
                space_start = None
        elif space_start is None:
            space_start = i
        i += 1

    ## Iterate through file_ids in reverse
    max_file_id = max(d for d in disk_map if d != ".")
    for file_id in range(max_file_id, -1, -1):

        ## Find the file length
        file_id_indices = {d for d in range(len(disk_map)) if disk_map[d] == file_id}
        file_length = max(file_id_indices) - min(file_id_indices) + 1

        ## Find spaces to the left that could fit the file, selecting the earliest
        valid_spaces = {
            space
            for space in space_map
            if space[1] >= file_length and space[0] < min(file_id_indices)
        }
        if not valid_spaces:
            continue
        selected_space = min(valid_spaces, key=lambda space: space[0])

        ## Remove the file from where it currently sits
        for i in file_id_indices:
            disk_map[i] = "."

        ## Place the file in the selected_space
        for s in range(selected_space[0], selected_space[0] + file_length):
            disk_map[s] = file_id

        ## Update the space map with the filled space
        space_map.remove(selected_space)
        space_map.add((selected_space[0] + file_length, selected_space[1] - file_length))


def compute_filesystem_checksum(disk_map: list[int, str]) -> int:

    filesystem_checksum = 0
    for position, id_number in enumerate(disk_map):
        if id_number != ".":
            filesystem_checksum += position * id_number

    return filesystem_checksum


if __name__ == "__main__":

    disk_map = expand_disk_map(import_input())
    compact_hard_drive(disk_map)

    print("Day 9 Part 2:", compute_filesystem_checksum(disk_map))
