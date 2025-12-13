from functools import cache


def import_input() -> dict[str, tuple[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    devices = {line.strip().split(": ")[0]: tuple(line.strip().split(": ")[1].split(" ")) for line in file_lines}
    return devices


def count_exit_paths(devices) -> int:

    @cache
    def count_future_paths(device_name, start_dac, start_fft) -> int:
        exit_paths = 0

        for output in devices[device_name]:
            dac = start_dac or output == "dac"
            fft = start_fft or output == "fft"

            if output == "out" and dac and fft:
                exit_paths += 1
            elif output == "out":
                continue
            else:
                exit_paths += count_future_paths(output, dac, fft)

        return exit_paths

    exit_paths = count_future_paths("svr", False, False)
    return exit_paths


if __name__ == "__main__":
    devices = import_input()
    exit_paths = count_exit_paths(devices)

    print("Day 11 Part 2:", exit_paths)
