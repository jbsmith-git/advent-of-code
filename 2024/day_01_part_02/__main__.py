def import_input() -> dict:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    location_ids = {"LEFT": [], "RIGHT": []}
    for line in lines:
        left_id, right_id = line.replace("\n", "").split("   ")
        location_ids["LEFT"].append(int(left_id))
        location_ids["RIGHT"].append(int(right_id))

    return location_ids


def compute_total_similarity_score(location_ids: dict) -> int:

    total_similarity_score = 0
    for left_id in location_ids["LEFT"]:
        total_similarity_score += left_id * location_ids["RIGHT"].count(left_id)

    return total_similarity_score


if __name__ == "__main__":

    location_ids = import_input()

    total_similarity_score = compute_total_similarity_score(location_ids)

    print("Day 1 Part 2:", total_similarity_score)
