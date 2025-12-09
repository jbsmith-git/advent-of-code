def import_input() -> tuple[tuple[int]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    red_tile_coords = tuple(tuple(map(int, line.split(","))) for line in file_lines)
    return red_tile_coords


if __name__ == "__main__":
    red_tile_coords = import_input()
    largest_red_rectangle_area = max(
        (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)
        for c1 in red_tile_coords
        for c2 in red_tile_coords
        if c1 != c2
    )

    print("Day 9 Part 1:", largest_red_rectangle_area)
