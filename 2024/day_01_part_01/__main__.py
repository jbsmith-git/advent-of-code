def import_input() -> dict:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    location_ids = {"LEFT": [], "RIGHT": []}
    for line in lines:
        left_id, right_id = line.replace("\n", "").split("   ")
        location_ids["LEFT"].append(int(left_id))
        location_ids["RIGHT"].append(int(right_id))

    return location_ids


def compute_total_diff(location_ids: dict) -> int:

    location_ids["LEFT"].sort()
    location_ids["RIGHT"].sort()

    total_diff = 0
    for left_id, right_id in zip(location_ids["LEFT"], location_ids["RIGHT"]):
        total_diff += abs(left_id - right_id)

    return total_diff


if __name__ == "__main__":

    location_ids = import_input()

    total_diff = compute_total_diff(location_ids)

    print("Day 1 Part 1:", total_diff)
