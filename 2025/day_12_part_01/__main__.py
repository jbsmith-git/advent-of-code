from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Shape:
    index: int
    layout: tuple[tuple[str]]

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.layout]) + "\n"

    @cached_property
    def variations(self) -> tuple[Shape]:
        (a, b, c), (d, e, f), (g, h, i) = self.layout

        shapes = {
            Shape(self.index, ((a, b, c), (d, e, f), (g, h, i))),  # original
            Shape(self.index, ((g, d, a), (h, e, b), (i, f, c))),  # original 90 clockwise
            Shape(self.index, ((i, h, g), (f, e, d), (c, b, a))),  # original 180
            Shape(self.index, ((c, f, i), (b, e, h), (a, d, g))),  # original 270 clockwise
            Shape(self.index, ((c, b, a), (f, e, d), (i, h, g))),  # reflection
            Shape(self.index, ((i, f, c), (h, e, b), (g, d, a))),  # reflection 90 clockwise
            Shape(self.index, ((g, h, i), (d, e, f), (a, b, c))),  # reflection 180
            Shape(self.index, ((a, d, g), (b, e, h), (c, f, i))),  # reflection 270 clockwise
        }

        return tuple(shapes)

    @cached_property
    def area(self) -> int:
        return sum(x == "#" for row in self.layout for x in row)


@dataclass(frozen=True)
class Region:
    width: int
    length: int
    shape_reqs: tuple[int]

    @cached_property
    def area(self) -> int:
        return self.width * self.length


def import_input() -> tuple[dict[int, Shape], tuple[Region]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    shapes = tuple(
        Shape(
            int(line.replace(":", "").strip()),
            tuple(
                [tuple(file_lines[l + 1].strip()), tuple(file_lines[l + 2].strip()), tuple(file_lines[l + 3].strip())]
            ),
        )
        for l, line in enumerate(file_lines)
        if ":" in line and "x" not in line
    )
    shapes = {shape.index: shape for shape in shapes}

    regions = tuple(
        Region(
            int(line.split(": ")[0].split("x")[0]),
            int(line.split(": ")[0].split("x")[1]),
            tuple(map(int, line.split(": ")[1].strip().split(" "))),
        )
        for l, line in enumerate(file_lines)
        if "x" in line
    )

    return shapes, regions


def check_region_validity(region: Region, shapes: dict[int, Shape]) -> bool:
    total_shape_area = sum(shapes[i].area * vol for i, vol in enumerate(region.shape_reqs))
    if total_shape_area > region.area:
        return False

    full_shape_spaces = (region.width // 3) * (region.length // 3)
    if full_shape_spaces >= sum(region.shape_reqs):
        return True

    raise Exception(f"The validity of {region} could not be determined")


if __name__ == "__main__":
    shapes, regions = import_input()
    valid_regions = sum(check_region_validity(region, shapes) for region in regions)

    print("Day 12 Part 1:", valid_regions)
