from dataclasses import dataclass, field
import itertools as it


@dataclass
class AntennaFrequencyGroup:
    frequency: str
    antennas: set[tuple]
    antinodes: set[tuple] = field(default_factory=set)


def import_input() -> list[AntennaFrequencyGroup]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    lines = tuple(tuple(line.replace("\n", "")) for line in lines)

    frequency_groups = {}
    row_count = len(lines)
    for r in range(row_count):
        for c, value in enumerate(lines[r]):

            if value == ".":
                continue

            ## Map (r, c) to standard coordinate system
            if value not in frequency_groups.keys():
                frequency_groups[value] = AntennaFrequencyGroup(value, {(row_count - r - 1, c)})
            else:
                frequency_groups[value].antennas.add((row_count - r - 1, c))

    return list(frequency_groups.values())


def compute_frequency_group_antinodes(frequency_group: AntennaFrequencyGroup) -> None:

    for a1, a2 in it.combinations(frequency_group.antennas, 2):

        a1_a2_vector = (a2[0] - a1[0], a2[1] - a1[1])
        antinode_1 = (a2[0] + a1_a2_vector[0], a2[1] + a1_a2_vector[1])
        antinode_2 = (a1[0] - a1_a2_vector[0], a1[1] - a1_a2_vector[1])

        for antinode in {antinode_1, antinode_2}:
            if 0 <= antinode[0] <= 49 and 0 <= antinode[1] <= 49:
                frequency_group.antinodes.add(antinode)


if __name__ == "__main__":

    frequency_groups = import_input()

    distinct_antinode_coords = set()
    for frequency_group in frequency_groups:
        compute_frequency_group_antinodes(frequency_group)
        distinct_antinode_coords.update(frequency_group.antinodes)

    print("Day 8 Part 1:", len(distinct_antinode_coords))
