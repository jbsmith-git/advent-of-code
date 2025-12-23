from itertools import product

from machine import Machine
from machine_matrix import MachineMatrix
from sympy.core.numbers import Integer as sympy_int


def import_input() -> tuple[Machine]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    machines = []
    for line in file_lines:
        joltage_reqs = tuple(map(int, line[line.index("{") + 1 : line.index("}")].split(",")))

        button_schemas = tuple(
            tuple(map(int, schematic.split(",")))
            for schematic in line[line.index("(") + 1 : line.index("{") - 2].split(") (")
        )

        machines.append(Machine(joltage_reqs, button_schemas))

    return tuple(machines)


def find_minimum_button_presses(machine: Machine) -> int:
    # Convert augmented matrix to RREF form
    rref_matrix, pivot_cols = machine.augmented_matrix.rref()
    rref_matrix = MachineMatrix.from_matrix(rref_matrix)
    rref_matrix.remove_zero_rows()

    lhs_matrix = rref_matrix.lhs
    rhs = rref_matrix.rhs

    # If the LHS is an identity matrix, there is a unique solution
    if lhs_matrix.is_Identity:
        return sum(rhs)

    # Otherwise, brute force the free variables to find the minimum solution
    free_var_cols = tuple(set(range(lhs_matrix.cols)).difference(set(pivot_cols)))
    minimum_button_presses = None
    for free_var_comb in product(range(max(machine.joltage_reqs) + 1), repeat=len(free_var_cols)):

        # Find the values of the non-free variables for this combination
        modified_rhs = tuple(
            val - sum(lhs_matrix.row(r)[c] * fv for c, fv in zip(free_var_cols, free_var_comb))
            for r, val in enumerate(rhs)
        )

        # If all non-free variables are non-negative ints, then we have a candidate solution
        if all(v >= 0 and isinstance(v, sympy_int) for v in modified_rhs):
            button_presses = sum(modified_rhs) + sum(free_var_comb)
            if minimum_button_presses is None:
                minimum_button_presses = button_presses
            else:
                minimum_button_presses = min(minimum_button_presses, button_presses)

    # Check nothing went wrong (that we found some solution)
    if minimum_button_presses is None:
        raise Exception(f"The minimum required button presses for {machine} could not be determined")

    return minimum_button_presses


if __name__ == "__main__":
    machines = import_input()
    minimum_button_presses = sum(map(find_minimum_button_presses, machines))

    print("Day 10 Part 2:", minimum_button_presses)
