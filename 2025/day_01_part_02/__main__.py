DIAL_STARTING_VALUE = 50


def import_input() -> tuple[str]:
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()

    rotations = tuple(line.strip() for line in input_lines)
    return rotations


def apply_rotations(rotations: tuple[str]) -> int:
    zero_count = 0
    dial_value = DIAL_STARTING_VALUE

    for rotation in rotations:
        clicks = int(rotation[1:])

        for _ in range(clicks):
            dial_value += 1 if "L" in rotation else -1
            dial_value %= 100
            if dial_value == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    rotations = import_input()
    zero_count = apply_rotations(rotations)

    print("Day 1 Part 2:", zero_count)
