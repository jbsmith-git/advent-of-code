from dataclasses import dataclass
from itertools import combinations


@dataclass
class Machine:
    indicator_lights: list[bool]
    indicator_light_diagram: tuple[bool]
    button_wiring_schematics: tuple[tuple[int]]
    joltage_requirements: tuple[int]

    def press_button(self, wiring_schematic: tuple[int]) -> None:
        if wiring_schematic not in self.button_wiring_schematics:
            raise ValueError("Button does not exist")
        for w in wiring_schematic:
            self.indicator_lights[w] = not self.indicator_lights[w]


def import_input() -> tuple[Machine]:
    with open("input.txt", "r") as input_file:
        file_lines = input_file.readlines()

    machines = []
    for line in file_lines:

        indicator_light_diagram = tuple(light == "#" for light in line[1 : line.index("]")])
        button_wiring_schematics = tuple(
            tuple(map(int, schematic.split(",")))
            for schematic in line[line.index("(") + 1 : line.index("{") - 2].split(") (")
        )
        joltage_requirements = tuple(map(int, line[line.index("{") + 1 : line.index("}")].split(",")))

        machine = Machine(
            [False for _ in range(len(indicator_light_diagram))],
            indicator_light_diagram,
            button_wiring_schematics,
            joltage_requirements,
        )
        machines.append(machine)

    return tuple(machines)


def find_minimum_button_presses(machine: Machine) -> int:
    # Each button only needs to be pressed up to once
    button_combos = tuple(
        combo
        for combo_group in (
            combinations(machine.button_wiring_schematics, r) for r in range(len(machine.button_wiring_schematics) + 1)
        )
        for combo in combo_group
    )

    minimum_presses = None
    for combo in button_combos:
        machine.indicator_lights = [False for _ in range(len(machine.indicator_light_diagram))]

        for button in combo:
            machine.press_button(button)

        if tuple(machine.indicator_lights) == machine.indicator_light_diagram:
            minimum_presses = len(combo) if minimum_presses is None else min(minimum_presses, len(combo))

    return minimum_presses


if __name__ == "__main__":
    machines = import_input()
    minimum_button_presses = sum(map(find_minimum_button_presses, machines))

    print("Day 10 Part 1:", minimum_button_presses)
