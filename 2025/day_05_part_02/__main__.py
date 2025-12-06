def import_input() -> tuple[tuple[int]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    fresh_id_ranges = tuple(tuple(int(id) for id in line.strip().split("-")) for line in file_lines if "-" in line)
    return fresh_id_ranges


def combine_id_ranges(fresh_id_ranges):
    fresh_id_ranges = list(set(fresh_id_ranges))

    def combine_range(id_ranges):
        for r, (lb, ub) in enumerate(id_ranges):
            for rc, (lbc, ubc) in enumerate(id_ranges):
                if r == rc:
                    continue
                if lbc <= lb and ub <= ubc:
                    id_ranges.pop(r)
                    return True
                if lb <= lbc and ubc <= ub:
                    id_ranges.pop(rc)
                    return True
                if lb <= ubc and ub > ubc:
                    id_ranges[r] = (ubc + 1, ub)
                    return True
                if ub >= lbc and lb < lbc:
                    id_ranges[r] = (lb, lbc - 1)
                    return True
        return False

    progress = True
    while progress:
        progress = combine_range(fresh_id_ranges)

    return fresh_id_ranges


if __name__ == "__main__":
    fresh_id_ranges = import_input()
    unique_fresh_ids = sum(ub - lb + 1 for lb, ub in combine_id_ranges(fresh_id_ranges))

    print("Day 5 Part 2:", unique_fresh_ids)
