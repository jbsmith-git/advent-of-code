from dataclasses import dataclass

from machine_matrix import MachineMatrix


@dataclass(slots=True)
class Machine:
    joltage_reqs: tuple[int]
    button_schemas: tuple[tuple[int]]
    augmented_matrix: MachineMatrix = None

    def __post_init__(self) -> None:
        """Combine the joltage deltas and reqs, transposing into an augmented matrix"""
        self.augmented_matrix = MachineMatrix(list(self.joltage_deltas) + [self.joltage_reqs]).T

    @property
    def joltage_deltas(self) -> tuple[tuple[int]]:
        """Convert the button schemas into a tuple of changes (1/0) to each joltage level"""
        return tuple(
            tuple((1 if r in schema else 0) for r in range(len(self.joltage_reqs))) for schema in self.button_schemas
        )
