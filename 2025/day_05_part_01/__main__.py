def import_input() -> tuple[tuple[tuple[int]], tuple[int]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    fresh_id_ranges = tuple(tuple(int(id) for id in line.strip().split("-")) for line in file_lines if "-" in line)
    available_ids = tuple(int(line.strip()) for line in file_lines if "-" not in line and line != "\n")

    return fresh_id_ranges, available_ids


def check_id_is_fresh(fresh_id_ranges: tuple[tuple[int]], id: int) -> bool:
    for lb, ub in fresh_id_ranges:
        if lb <= id <= ub:
            return True
    return False


if __name__ == "__main__":
    fresh_id_ranges, available_ids = import_input()
    fresh_id_count = sum(check_id_is_fresh(fresh_id_ranges, id) for id in available_ids)

    print("Day 5 Part 1:", fresh_id_count)
