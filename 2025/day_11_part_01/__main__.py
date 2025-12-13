from functools import cache


def import_input() -> dict[str, tuple[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    devices = {line.strip().split(": ")[0]: tuple(line.strip().split(": ")[1].split(" ")) for line in file_lines}
    return devices


def count_exit_paths(devices) -> int:

    @cache
    def count_future_paths(device_name) -> int:
        return sum(1 if output == "out" else count_future_paths(output) for output in devices[device_name])

    exit_paths = count_future_paths("you")
    return exit_paths


if __name__ == "__main__":
    devices = import_input()
    exit_paths = count_exit_paths(devices)

    print("Day 11 Part 1:", exit_paths)
