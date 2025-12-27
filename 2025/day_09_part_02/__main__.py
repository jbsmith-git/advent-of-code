from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)

    @property
    def opposite(self) -> Direction:
        return Direction((-self.value[0], -self.value[1]))

    def is_perpendicular(self, other: Direction) -> bool:
        return (self.value[0] * other.value[0]) + (self.value[1] * other.value[1]) == 0


@dataclass(eq=False, frozen=True, slots=True)
class BorderTile:
    x: int
    y: int
    inside_directions: tuple[Direction]


def import_input() -> tuple[tuple[int]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    red_tile_coords = tuple(tuple(map(int, line.split(","))) for line in file_lines)
    return red_tile_coords


def find_all_tile_coords(red_tile_coords: tuple[tuple[int]]) -> tuple[tuple[int]]:
    all_tile_coords = []

    for c, coords in enumerate(red_tile_coords):
        prev_coords = red_tile_coords[c - 1]

        if prev_coords[0] == coords[0]:
            direction = (0, 1) if prev_coords[1] < coords[1] else (0, -1)
            distance = abs(coords[1] - prev_coords[1])
        else:
            direction = (1, 0) if prev_coords[0] < coords[0] else (-1, 0)
            distance = abs(coords[0] - prev_coords[0])

        for d in range(1, distance + 1):
            all_tile_coords.append((prev_coords[0] + direction[0] * d, prev_coords[1] + direction[1] * d))

    return tuple(all_tile_coords)


def calculate_tile_directions(all_tile_coords: tuple[tuple[int]]) -> tuple[BorderTile]:
    border_tiles = []
    inside_direction = Direction.EAST  # Initially the inside is to the East (trial and error)

    for c, coords in enumerate(all_tile_coords):
        prev_coords_1 = all_tile_coords[c - 1]
        prev_coords_2 = all_tile_coords[c - 2]
        next_coords_1 = all_tile_coords[(c + 1) % len(all_tile_coords)]

        prev_direction = Direction((prev_coords_1[0] - prev_coords_2[0], prev_coords_1[1] - prev_coords_2[1]))
        direction = Direction((coords[0] - prev_coords_1[0], coords[1] - prev_coords_1[1]))
        next_direction = Direction((next_coords_1[0] - coords[0], next_coords_1[1] - coords[1]))

        # On a straight section
        if direction == prev_direction and direction == next_direction:
            border_tiles.append(BorderTile(coords[0], coords[1], (inside_direction,)))

        # About to turn a corner
        elif direction == prev_direction and direction.is_perpendicular(next_direction):
            if next_direction == inside_direction:
                border_tiles.append(BorderTile(coords[0], coords[1], tuple()))
                inside_direction = direction.opposite
            else:
                border_tiles.append(BorderTile(coords[0], coords[1], (inside_direction, direction)))
                inside_direction = direction

        # Just turned a corner
        elif direction.is_perpendicular(prev_direction) and direction == next_direction:
            border_tiles.append(BorderTile(coords[0], coords[1], (inside_direction,)))

        # Just turned a corner and now turning another
        else:
            raise Exception("An unhandled edge case arose when calculating tile directions")

    return tuple(border_tiles)


def find_rectangle_border_coords(corner_1_coords: tuple[int], corner_2_coords: tuple[int]) -> tuple[tuple[int]]:
    width = abs(corner_1_coords[0] - corner_2_coords[0])
    height = abs(corner_1_coords[1] - corner_2_coords[1])

    border_tiles_x = [(corner_1_coords[0] + d, corner_1_coords[1]) for d in range(width + 1)]
    border_tiles_x += [(corner_1_coords[0] + d, corner_2_coords[1]) for d in range(width + 1)]

    if corner_1_coords[1] <= corner_2_coords[1]:
        border_tiles_y = [(corner_1_coords[0], corner_1_coords[1] + d) for d in range(height + 1)]
        border_tiles_y += [(corner_2_coords[0], corner_2_coords[1] - d) for d in range(height + 1)]
    else:
        border_tiles_y = [(corner_1_coords[0], corner_1_coords[1] - d) for d in range(height + 1)]
        border_tiles_y += [(corner_2_coords[0], corner_2_coords[1] + d) for d in range(height + 1)]

    return tuple(set(border_tiles_x + border_tiles_y))


def find_largest_valid_rectangle_area(border_tiles: tuple[BorderTile], red_tile_coords: tuple[tuple[int]]) -> int:
    border_tile_lookup = {(tile.x, tile.y): tile for tile in border_tiles}
    border_tile_coords = set(border_tile_lookup.keys())
    min_x = min(tile.x for tile in border_tiles)

    def validate_border_coords(bx: int, by: int) -> bool:
        if (bx, by) in border_tile_coords:
            return True

        # Look to the left to see if the first border points East
        for lx in range(bx - 1, min_x - 1, -1):
            if (lx, by) in border_tile_coords:
                return Direction.EAST in border_tile_lookup[(lx, by)].inside_directions

        return False

    largest_area = 0
    for c1 in red_tile_coords:
        for c2 in red_tile_coords:

            # Can assume that c1 comes before c2 on the x-axis
            if c1 == c2 or c1[0] > c2[0]:
                continue

            # Don't bother checking validity if the area is too small
            area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)
            if area <= largest_area:
                continue

            border_coords = find_rectangle_border_coords(c1, c2)
            if all(validate_border_coords(bx, by) for bx, by in border_coords):
                largest_area = area

    return largest_area


if __name__ == "__main__":
    red_tile_coords = import_input()
    all_tile_coords = find_all_tile_coords(red_tile_coords)

    border_tiles = calculate_tile_directions(all_tile_coords)
    largest_rectangle_area = find_largest_valid_rectangle_area(border_tiles, red_tile_coords)

    print("Day 9 Part 2:", largest_rectangle_area)
