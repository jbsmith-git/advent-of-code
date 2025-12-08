from __future__ import annotations

import math
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


def connect_junction_boxes(junction_boxes: dict[int, JunctionBox]) -> tuple[int, int]:
    distances = [
        (jb1_id, jb2_id, jb1 - jb2)
        for jb1_id, jb1 in junction_boxes.items()
        for jb2_id, jb2 in junction_boxes.items()
        if jb1_id < jb2_id
    ]
    distances.sort(key=lambda x: x[2])

    i = 0
    while len(set(jb.circuit_id for jb in junction_boxes.values())) > 1:
        jb1 = junction_boxes[distances[i][0]]
        jb2 = junction_boxes[distances[i][1]]

        if jb1.circuit_id != jb2.circuit_id:
            new_circuit_id, old_circuit_id = jb1.circuit_id, jb2.circuit_id

            for jb_id, jb in junction_boxes.items():
                if jb.circuit_id == old_circuit_id:
                    junction_boxes[jb_id].circuit_id = new_circuit_id

        i += 1

    return distances[i - 1][0], distances[i - 1][1]


if __name__ == "__main__":
    junction_boxes = import_input()

    final_jb1_id, final_jb2_id = connect_junction_boxes(junction_boxes)
    final_connection_product = junction_boxes[final_jb1_id].coords[0] * junction_boxes[final_jb2_id].coords[0]

    print("Day 8 Part 2:", final_connection_product)
