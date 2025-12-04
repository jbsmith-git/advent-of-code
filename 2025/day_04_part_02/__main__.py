def import_input() -> list[list[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    grid = [list(line.strip()) for line in file_lines]
    return grid


def count_removable_rolls(grid: list[list[str]]) -> int:
    removable_rolls = 0

    some_rolls_removed = True
    while some_rolls_removed:
        some_rolls_removed = False

        for r, row in enumerate(grid):
            for c, object in enumerate(row):
                if object != "@":
                    continue

                surrounding_rolls = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(row):
                            if (dr != 0 or dc != 0) and grid[r + dr][c + dc] == "@":
                                surrounding_rolls += 1

                if surrounding_rolls <= 3:
                    removable_rolls += 1
                    grid[r][c] = "."
                    some_rolls_removed = True

    return removable_rolls


if __name__ == "__main__":
    grid = import_input()
    removable_rolls = count_removable_rolls(grid)

    print("Day 4 Part 2:", removable_rolls)
