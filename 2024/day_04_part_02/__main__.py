import itertools as it


def import_input() -> tuple[str]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    word_search = tuple(line.replace("\n", "") for line in lines)

    return word_search


def count_x_mas(word_search: tuple[str]) -> int:

    x_mas_layouts = {
        ((-1, 1, "M"), (1, 1, "M"), (-1, -1, "S"), (1, -1, "S")),
        ((-1, 1, "M"), (1, 1, "S"), (-1, -1, "M"), (1, -1, "S")),
        ((-1, 1, "S"), (1, 1, "S"), (-1, -1, "M"), (1, -1, "M")),
        ((-1, 1, "S"), (1, 1, "M"), (-1, -1, "S"), (1, -1, "M")),
    }

    x_mas_count = 0
    height, width = len(word_search), len(word_search[0])
    for r, c in it.product(range(1, height - 1), range(1, width - 1)):

        if word_search[r][c] != "A":
            continue

        for layout in x_mas_layouts:
            layout_checks = {word_search[r + h][c + v] == l for h, v, l in layout}
            if layout_checks == {True}:
                x_mas_count += 1

    return x_mas_count


if __name__ == "__main__":

    word_search = import_input()

    x_mas_count = count_x_mas(word_search)

    print("Day 4 Part 2:", x_mas_count)
