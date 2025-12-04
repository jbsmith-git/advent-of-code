def import_input() -> list[list[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    grid = [list(line.strip()) for line in file_lines]
    return grid


def count_accessible_rolls(grid: list[list[str]]) -> int:
    accessible_rolls = 0

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
                accessible_rolls += 1

    return accessible_rolls


if __name__ == "__main__":
    grid = import_input()
    accessible_rolls = count_accessible_rolls(grid)

    print("Day 4 Part 1:", accessible_rolls)
