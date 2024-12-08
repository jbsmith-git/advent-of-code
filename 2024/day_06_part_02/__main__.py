import copy


def import_input() -> list[list]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    patrol_map = [list(line.replace("\n", "")) for line in lines]

    return patrol_map


def infinite_patrol_check(patrol_map: list[list]) -> bool:

    height = len(patrol_map)
    width = len(patrol_map[0])

    for r in range(height):
        for c in range(width):
            if patrol_map[r][c] == "^":
                guard_r, guard_c = r, c

    caret_move_map = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    caret_turn_map = {"^": ">", ">": "v", "v": "<", "<": "^"}

    patrol_history = set()
    while True:

        if (guard_r, guard_c, patrol_map[guard_r][guard_c]) in patrol_history:
            return True
        else:
            patrol_history.add((guard_r, guard_c, patrol_map[guard_r][guard_c]))

        move = caret_move_map[patrol_map[guard_r][guard_c]]
        new_guard_r, new_guard_c = guard_r + move[0], guard_c + move[1]

        if not (0 <= new_guard_r < height and 0 <= new_guard_c < width):
            return False

        if patrol_map[new_guard_r][new_guard_c] == "#":
            patrol_map[guard_r][guard_c] = caret_turn_map[patrol_map[guard_r][guard_c]]
        else:
            patrol_map[new_guard_r][new_guard_c], patrol_map[guard_r][guard_c] = (
                patrol_map[guard_r][guard_c],
                patrol_map[new_guard_r][new_guard_c],
            )
            guard_r, guard_c = new_guard_r, new_guard_c


if __name__ == "__main__":

    patrol_map = import_input()
    patrol_map_copy = copy.deepcopy(patrol_map)

    new_obstruction_positions = 0
    for r in range(len(patrol_map)):
        for c in range(len(patrol_map[0])):
            if patrol_map[r][c] == ".":
                patrol_map[r][c] = "#"
                if infinite_patrol_check(patrol_map):
                    new_obstruction_positions += 1
                patrol_map = copy.deepcopy(patrol_map_copy)

    print("Day 6 Part 2:", new_obstruction_positions)
