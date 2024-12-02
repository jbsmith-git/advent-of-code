def import_input() -> list:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    reports = []
    for line in lines:
        line = line.replace("\n", "")
        report = tuple([int(l) for l in line.split(" ")])
        reports.append(report)

    return reports


def report_safety(report: tuple) -> bool:

    unique_diffs = {report[l + 1] - report[l] for l in range(0, len(report) - 1)}
    diff_signs = {d > 0 for d in unique_diffs}

    return len(diff_signs) == 1 and unique_diffs.issubset({-3, -2, -1, 1, 2, 3})


if __name__ == "__main__":

    reports = import_input()

    unsafe_report_count = sum(report_safety(r) for r in reports)

    print("Day 2 Part 1:", unsafe_report_count)
