import itertools as it
from dataclasses import dataclass


@dataclass(frozen=True)
class Equation:
    test_value: str
    numbers: tuple[str]


def import_input() -> set[Equation]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    calibration_equations = set()
    for line in lines:
        line = line.replace("\n", "")
        equation = Equation(line.split(":")[0], tuple(line.split(" ")[1:]))
        calibration_equations.add(equation)

    return calibration_equations


def check_equation_possible(equation: Equation) -> bool:

    for operator_combination in it.product({"+", "*", "||"}, repeat=len(equation.numbers) - 1):

        expression = list(equation.numbers)
        for i, oc in enumerate(operator_combination):
            expression.insert(2 * i + 1, oc)

        while len(expression) > 1:
            sub_expression = expression[:3]
            if "||" in sub_expression:
                sub_expression_value = sub_expression[0] + sub_expression[2]
            else:
                sub_expression_string = "".join(sub_expression)
                sub_expression_value = str(eval(sub_expression_string))
            expression = [sub_expression_value] + expression[3:]

        if expression[0] == equation.test_value:
            return True

    return False


if __name__ == "__main__":

    calibration_equations = import_input()

    test_value_sum = 0
    for equation in calibration_equations:
        if check_equation_possible(equation):
            test_value_sum += int(equation.test_value)

    print("Day 7 Part 2:", test_value_sum)
