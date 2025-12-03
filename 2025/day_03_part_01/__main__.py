def import_input() -> tuple[list[int]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    banks = tuple([int(joltage) for joltage in line.strip()] for line in file_lines)
    return banks


def find_maximum_joltage(bank: list[int]) -> int:
    maximum_joltage_d1 = max(bank[:-1])
    maximum_joltage_d2 = max(bank[bank.index(maximum_joltage_d1) + 1 :])

    maximum_joltage = 10 * maximum_joltage_d1 + maximum_joltage_d2
    return maximum_joltage


if __name__ == "__main__":
    banks = import_input()
    total_output_joltage = sum(find_maximum_joltage(bank) for bank in banks)

    print("Day 3 Part 1:", total_output_joltage)
