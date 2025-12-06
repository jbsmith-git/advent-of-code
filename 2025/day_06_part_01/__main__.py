import math


def import_input() -> list[list[str]]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    file_lines = tuple(tuple(line.split()) for line in file_lines)

    problems = [[] for p in range(len(file_lines[0]))]
    for line in file_lines:
        for v, value in enumerate(line):
            problems[v].append(value)

    return problems


def solve_problem(problem: list[str]) -> int:
    if problem[-1] == "+":
        return sum(int(v) for v in problem[:-1])
    if problem[-1] == "*":
        return math.prod(int(v) for v in problem[:-1])

    raise ValueError("Operator not recognised")


if __name__ == "__main__":
    problems = import_input()
    grand_total = sum(solve_problem(problem) for problem in problems)

    print("Day 6 Part 1:", grand_total)
