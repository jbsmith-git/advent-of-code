import itertools as it


def import_input() -> tuple[str]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    word_search = tuple(line.replace("\n", "") for line in lines)

    return word_search


def count_xmas(word_search: tuple[str]) -> int:

    word_directions = {
        ## Orthogonal directions
        ((1, 0), (2, 0), (3, 0)),
        ((-1, 0), (-2, 0), (-3, 0)),
        ((0, 1), (0, 2), (0, 3)),
        ((0, -1), (0, -2), (0, -3)),
        ## Diagonal directions
        ((1, 1), (2, 2), (3, 3)),
        ((-1, -1), (-2, -2), (-3, -3)),
        ((-1, 1), (-2, 2), (-3, 3)),
        ((1, -1), (2, -2), (3, -3)),
    }

    xmas_count = 0
    height, width = len(word_search), len(word_search[0])
    for r, c in it.product(range(height), range(width)):
        letter = word_search[r][c]

        if letter != "X":
            continue

        for direction in word_directions:

            ## Check if in bounds
            row_lb = min({r + h for h, v in direction}) >= 0
            row_ub = max({r + h for h, v in direction}) <= width - 1
            col_lb = min({c + v for h, v in direction}) >= 0
            col_ub = max({c + v for h, v in direction}) <= height - 1
            if not (row_lb and row_ub and col_lb and col_ub):
                continue

            ## Check if the MAS is in the direction
            if [word_search[r + h][c + v] for h, v in direction] == ["M", "A", "S"]:
                xmas_count += 1

    return xmas_count


if __name__ == "__main__":

    word_search = import_input()

    xmas_count = count_xmas(word_search)

    print("Day 4 Part 1:", xmas_count)
