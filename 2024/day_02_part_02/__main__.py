def import_input() -> list:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    reports = []
    for line in lines:
        line = line.replace("\n", "")
        report = [int(l) for l in line.split(" ")]
        reports.append(report)

    return reports


def subreport_safety(subreport: list) -> bool:

    unique_diffs = {subreport[l + 1] - subreport[l] for l in range(0, len(subreport) - 1)}
    diff_signs = {d > 0 for d in unique_diffs}

    return len(diff_signs) == 1 and unique_diffs.issubset({-3, -2, -1, 1, 2, 3})


def report_safety(report: list) -> bool:

    if subreport_safety(report):
        return True

    for l in range(len(report)):
        removed_level = report.pop(l)
        if subreport_safety(report):
            return True
        report.insert(l, removed_level)

    return False


if __name__ == "__main__":

    reports = import_input()

    unsafe_report_count = sum(report_safety(r) for r in reports)

    print("Day 2 Part 2:", unsafe_report_count)
