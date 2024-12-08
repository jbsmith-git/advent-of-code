def import_input() -> list[list]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    patrol_map = [list(line.replace("\n", "")) for line in lines]

    return patrol_map


def plot_patrol(patrol_map: list[list]) -> None:

    height = len(patrol_map)
    width = len(patrol_map[0])

    for r in range(height):
        for c in range(width):
            if patrol_map[r][c] == "^":
                guard_r, guard_c = r, c

    caret_move_map = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    caret_turn_map = {"^": ">", ">": "v", "v": "<", "<": "^"}

    while True:

        # for row in patrol_map[guard_r - 5 : guard_r + 6]:
        #     print("".join(row[guard_c - 5 : guard_c + 6]))
        # print("")

        move = caret_move_map[patrol_map[guard_r][guard_c]]
        new_guard_r, new_guard_c = guard_r + move[0], guard_c + move[1]

        if not (0 <= new_guard_r < height and 0 <= new_guard_c < width):
            patrol_map[guard_r][guard_c] = "X"
            return patrol_map

        if patrol_map[new_guard_r][new_guard_c] == "#":
            patrol_map[guard_r][guard_c] = caret_turn_map[patrol_map[guard_r][guard_c]]
        else:
            patrol_map[new_guard_r][new_guard_c] = patrol_map[guard_r][guard_c]
            patrol_map[guard_r][guard_c] = "X"
            guard_r, guard_c = new_guard_r, new_guard_c


if __name__ == "__main__":

    patrol_map = import_input()

    plot_patrol(patrol_map)
    # for row in patrol_map:
    #     print("".join(row))

    unique_guard_positions = sum(p == "X" for row in patrol_map for p in row)

    print("Day 6 Part 1:", unique_guard_positions)
