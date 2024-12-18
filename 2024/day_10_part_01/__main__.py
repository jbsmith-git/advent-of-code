from dataclasses import dataclass


@dataclass
class TopographicPosition:
    height: int
    next_positions: set[tuple[int]]


def import_input() -> tuple[tuple[int]]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    topographic_map = []
    for line in lines:
        row = tuple(int(p) for p in line.replace("\n", ""))
        topographic_map.append(row)

    return tuple(topographic_map)


def find_topographic_positions(
    topographic_map: tuple[tuple[int]],
) -> dict[tuple[int], TopographicPosition]:

    map_height = len(topographic_map)
    map_width = len(topographic_map[0])

    topographic_positions = {}

    for r, row in enumerate(topographic_map):
        for c, height in enumerate(row):

            next_positions = []
            adjacent_coords = {(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)}
            for x, y in adjacent_coords:
                if 0 <= x <= map_width - 1 and 0 <= y <= map_height - 1:
                    if topographic_map[x][y] == height + 1:
                        next_positions.append((x, y))

            topographic_positions[(r, c)] = TopographicPosition(height, tuple(next_positions))

    return topographic_positions


def compute_trailhead_score(
    topographic_positions: dict[tuple[int], TopographicPosition], trailhead: tuple[int]
) -> int:

    active_coords = {trailhead}

    ## After 9 steps, any remaining positions are of height 9
    for _ in range(9):
        active_coords = {
            next_pos
            for x, y in active_coords
            for next_pos in topographic_positions[(x, y)].next_positions
        }

    return len(active_coords)


if __name__ == "__main__":

    topographic_map = import_input()
    topographic_positions = find_topographic_positions(topographic_map)

    trailhead_score_sum = 0
    for (x, y), position in topographic_positions.items():
        if position.height == 0:
            trailhead_score_sum += compute_trailhead_score(topographic_positions, (x, y))

    print("Day 10 Part 1:", trailhead_score_sum)
