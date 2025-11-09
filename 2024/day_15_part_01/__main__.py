from enum import StrEnum


class Object(StrEnum):
    ROBOT = "@"
    BOX = "O"
    WALL = "#"
    EMPTY = "."


class Move(StrEnum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

    @property
    def direction(self) -> tuple:
        return {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}[self.name]


def import_input() -> tuple:
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    warehouse_map = {
        (r, c): Object(object)
        for r, row in enumerate([tuple(line.strip()) for line in lines[0:50]])
        for c, object in enumerate(row)
    }
    moves = tuple(Move(move) for move in tuple("".join([line.strip() for line in lines[51:71]])))

    return warehouse_map, moves


def apply_move(warehouse_map: dict, move: Move) -> None:
    robot_coords = [(r, c) for (r, c), object in warehouse_map.items() if object == Object.ROBOT][0]

    distance = 0
    while True:
        distance += 1
        object = warehouse_map[
            (distance * move.direction[0] + robot_coords[0], distance * move.direction[1] + robot_coords[1])
        ]

        if object == Object.WALL:
            return
        if object == Object.EMPTY:
            break

    for step in range(distance - 1, -1, -1):
        warehouse_map[
            ((step + 1) * move.direction[0] + robot_coords[0], (step + 1) * move.direction[1] + robot_coords[1])
        ] = warehouse_map[(step * move.direction[0] + robot_coords[0], step * move.direction[1] + robot_coords[1])]

    warehouse_map[robot_coords] = Object.EMPTY


if __name__ == "__main__":
    warehouse_map, moves = import_input()

    for move in moves:
        apply_move(warehouse_map, move)

    gps_sum = sum(100 * r + c for (r, c), object in warehouse_map.items() if object == Object.BOX)

    print("Day 15 Part 1:", gps_sum)
