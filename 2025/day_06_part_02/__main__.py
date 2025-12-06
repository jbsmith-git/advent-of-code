import math
from dataclasses import dataclass, field


@dataclass
class Problem:
    operator: str = None
    values: list[int] = field(default_factory=list)

    def solve(self) -> int:
        if self.operator == "+":
            return sum(self.values)
        if self.operator == "*":
            return math.prod(self.values)


def import_input() -> list[Problem]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    file_lines = tuple(tuple(str(line)) for line in file_lines)

    problems = [Problem()]
    for c in range(len(file_lines[0]) - 1):
        column = tuple(line[c] for line in file_lines)
        if all(value == " " for value in column):
            problems.append(Problem())
            continue
        if column[-1] in {"+", "*"}:
            problems[-1].operator = column[-1]
        if any(value != " " for value in column[:-1]):
            problems[-1].values.append(int("".join(column[:-1])))

    return problems


if __name__ == "__main__":
    problems = import_input()
    grand_total = sum(problem.solve() for problem in problems)

    print("Day 6 Part 2:", grand_total)
