import copy


def import_input() -> tuple[list[int]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    banks = tuple([int(joltage) for joltage in line.strip()] for line in file_lines)
    return banks


def find_maximum_joltage(bank: list[int]) -> int:
    maximum_joltage = 0
    candidates = copy.deepcopy(bank)

    for b in range(12, 0, -1):
        best_joltage = max(candidates[: len(candidates) - b + 1])
        maximum_joltage += 10 ** (b - 1) * best_joltage
        candidates = candidates[candidates.index(best_joltage) + 1 :]

    return maximum_joltage


if __name__ == "__main__":
    banks = import_input()
    total_output_joltage = sum(find_maximum_joltage(bank) for bank in banks)

    print("Day 3 Part 2:", total_output_joltage)
