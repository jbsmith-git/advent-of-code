from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass


@dataclass(slots=True, eq=False)
class JunctionBox:
    id: int
    coords: tuple[int]
    circuit_id: int

    def __sub__(self, other: JunctionBox) -> float:
        return math.sqrt(
            (self.coords[0] - other.coords[0]) ** 2
            + (self.coords[1] - other.coords[1]) ** 2
            + (self.coords[2] - other.coords[2]) ** 2
        )


def import_input() -> dict[int, JunctionBox]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    junction_boxes = {
        l + 1: JunctionBox(l + 1, tuple(int(c) for c in line.strip().split(",")), l + 1)
        for l, line in enumerate(file_lines)
    }
    return junction_boxes


def connect_closest_junction_boxes(junction_boxes: dict[int, JunctionBox], connections: int) -> None:
    distances = [
        (jb1_id, jb2_id, jb1 - jb2)
        for jb1_id, jb1 in junction_boxes.items()
        for jb2_id, jb2 in junction_boxes.items()
        if jb1_id < jb2_id
    ]
    distances.sort(key=lambda x: x[2])

    for c in range(connections):
        jb1 = junction_boxes[distances[c][0]]
        jb2 = junction_boxes[distances[c][1]]

        if jb1.circuit_id != jb2.circuit_id:
            new_circuit_id, old_circuit_id = jb1.circuit_id, jb2.circuit_id

            for jb_id, jb in junction_boxes.items():
                if jb.circuit_id == old_circuit_id:
                    junction_boxes[jb_id].circuit_id = new_circuit_id


if __name__ == "__main__":
    junction_boxes = import_input()
    connect_closest_junction_boxes(junction_boxes, 1000)

    counter = Counter([jb.circuit_id for jb in junction_boxes.values()])
    biggest_circuit_size_product = math.prod(sorted(list(counter.values()), reverse=True)[:3])

    print("Day 8 Part 1:", biggest_circuit_size_product)
