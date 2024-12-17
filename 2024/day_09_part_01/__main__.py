def import_input() -> list[int]:

    with open("input.txt", "r") as input_file:
        line = input_file.readlines()[0]

    disk_map = [int(i) for i in line.replace("\n", "")]

    return disk_map


def expand_disk_map(disk_map: list[int]) -> list[int, str]:

    expanded_disk_map = []
    for i, data in enumerate(disk_map):

        if i % 2 == 1:
            expanded_disk_map.extend(list("." * data))
        else:
            expanded_disk_map.extend([i // 2 for d in range(data)])

    return expanded_disk_map


def compact_hard_drive(disk_map: list[int, str]) -> list[int]:

    while "." in disk_map:

        first_space = disk_map.index(".")
        disk_map[first_space], disk_map[-1] = disk_map[-1], disk_map[first_space]

        while disk_map[-1] == ".":
            disk_map.pop(-1)


def compute_filesystem_checksum(disk_map: list[int]) -> int:

    filesystem_checksum = 0
    for position, id_number in enumerate(disk_map):
        filesystem_checksum += position * id_number

    return filesystem_checksum


if __name__ == "__main__":

    disk_map = expand_disk_map(import_input())
    compact_hard_drive(disk_map)

    print("Day 9 Part 1:", compute_filesystem_checksum(disk_map))
