def import_input() -> list[list[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    manifold_diagram = [list(line) for line in file_lines]
    return manifold_diagram


def map_tachyon_beam(manifold_diagram: list[list[str]]) -> None:
    for r, row in enumerate(manifold_diagram):
        for c, object in enumerate(row):
            if object == "S":
                manifold_diagram[r + 1][c] = "|"
            elif object == "^" and manifold_diagram[r - 1][c] == "|":
                manifold_diagram[r][c - 1] = "|"
                manifold_diagram[r][c + 1] = "|"
            elif object == "." and manifold_diagram[r - 1][c] == "|":
                manifold_diagram[r][c] = "|"


def count_tachyon_beam_splits(manifold_diagram: list[list[str]]) -> int:
    tachyon_beam_splits = 0

    for r, row in enumerate(manifold_diagram):
        for c, object in enumerate(row):
            if object == "^" and manifold_diagram[r - 1][c] == "|":
                tachyon_beam_splits += 1

    return tachyon_beam_splits


if __name__ == "__main__":
    manifold_diagram = import_input()
    map_tachyon_beam(manifold_diagram)
    tachyon_beam_splits = count_tachyon_beam_splits(manifold_diagram)

    print("Day 7 Part 1:", tachyon_beam_splits)
