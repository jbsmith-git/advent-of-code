from functools import cache


def import_input() -> list[list[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    manifold_diagram = [list(line) for line in file_lines]
    return manifold_diagram


def map_tachyon_particle_paths(manifold_diagram: list[list[str]]) -> None:
    for r, row in enumerate(manifold_diagram):
        for c, object in enumerate(row):
            if object == "S":
                manifold_diagram[r + 1][c] = "|"
            elif object == "^" and manifold_diagram[r - 1][c] == "|":
                manifold_diagram[r][c - 1] = "|"
                manifold_diagram[r][c + 1] = "|"
            elif object == "." and manifold_diagram[r - 1][c] == "|":
                manifold_diagram[r][c] = "|"


def count_tachyon_particle_timelines(manifold_diagram: list[list[str]]) -> int:

    @cache
    def count_timelines(r: int, c: int) -> int:
        if r >= len(manifold_diagram):
            return 1
        if manifold_diagram[r][c] == "|":
            return count_timelines(r + 1, c)
        if manifold_diagram[r][c] == "^":
            return count_timelines(r + 1, c - 1) + count_timelines(r + 1, c + 1)

    sr, sc = [(r, c) for r, row in enumerate(manifold_diagram) for c, object in enumerate(row) if object == "S"][0]
    tachyon_particle_timelines = count_timelines(sr + 1, sc)

    return tachyon_particle_timelines


if __name__ == "__main__":
    manifold_diagram = import_input()
    map_tachyon_particle_paths(manifold_diagram)
    tachyon_particle_timelines = count_tachyon_particle_timelines(manifold_diagram)

    print("Day 7 Part 2:", tachyon_particle_timelines)
