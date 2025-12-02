def import_input() -> tuple[str]:
    with open("input.txt", "r") as input_file:
        contents = input_file.read()

    id_ranges = tuple(tuple(int(id) for id in line.split("-")) for line in contents.split(","))
    return id_ranges


def find_invalid_ids(id_ranges: tuple[tuple[int]]) -> int:
    invalid_id_sum = 0

    for lb, ub in id_ranges:
        for id in range(lb, ub + 1):
            invalid_ids = {
                str(id)[:id_sublength] * sequence_length
                for id_sublength in range(1, len(str(id)) // 2 + 1)
                for sequence_length in range(2, len(str(id)) // id_sublength + 1)
                if id_sublength * sequence_length == len(str(id))
            }
            if str(id) in invalid_ids:
                invalid_id_sum += id

    return invalid_id_sum


if __name__ == "__main__":
    id_ranges = import_input()
    invalid_id_sum = find_invalid_ids(id_ranges)

    print("Day 2 Part 2:", invalid_id_sum)
