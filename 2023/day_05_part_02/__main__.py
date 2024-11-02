from dataclasses import dataclass
import random


@dataclass(frozen=True)
class ValueMap:
    input_lb: int
    input_ub: int
    output_lb: int
    output_ub: int


@dataclass
class TypeMap:
    input_type: str
    output_type: str
    value_maps: set[ValueMap]


def apply_type_map_on_ranges(type_map, unmapped_ranges: set[tuple]) -> set:

    mapped_ranges = set()
    while len(unmapped_ranges) > 0:

        range = random.choice(tuple(unmapped_ranges))

        ## Deal with some edge cases
        if range[1] < range[0]:
            unmapped_ranges.remove(range)
            continue

        value_map_applied = False
        for value_map in type_map.value_maps:

            ## Value map covers whole range
            if value_map.input_lb <= range[0] and value_map.input_ub >= range[1]:
                mapped_ranges.add(
                    (
                        value_map.output_lb + (range[0] - value_map.input_lb),
                        value_map.output_lb + (range[1] - value_map.input_lb),
                    )
                )
                value_map_applied = True

            ## Value map is contained by range
            elif value_map.input_lb >= range[0] and value_map.input_ub <= range[1]:
                unmapped_ranges.add((range[0], value_map.input_lb - 1))
                mapped_ranges.add((value_map.output_lb, value_map.output_ub))
                unmapped_ranges.add((value_map.input_ub + 1, range[1]))
                value_map_applied = True

            ## Value map intersects with bottom of range
            elif value_map.input_lb < range[0] and range[0] <= value_map.input_ub <= range[1]:
                mapped_ranges.add(
                    (
                        value_map.output_lb + (range[0] - value_map.input_lb),
                        value_map.output_ub,
                    )
                )
                unmapped_ranges.add((value_map.input_ub + 1, range[1]))
                value_map_applied = True

            ## Value map intersects with top of range
            elif value_map.input_ub > range[1] and range[0] <= value_map.input_lb <= range[1]:
                unmapped_ranges.add((range[0], value_map.input_lb - 1))
                mapped_ranges.add(
                    (
                        value_map.output_lb,
                        value_map.output_lb + (range[1] - value_map.input_lb),
                    )
                )
                value_map_applied = True

            if value_map_applied:
                unmapped_ranges.remove(range)
                break

        ## If no value map applies then input range = output range
        if not value_map_applied:
            mapped_ranges.add(range)
            unmapped_ranges.remove(range)

    return mapped_ranges


def import_input() -> tuple[set[tuple], tuple[TypeMap]]:

    ## Read lines from file
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    ## Extract seed ranges
    seed_ranges = set()
    seed_line = [int(s) for s in lines[0][7:-1].split(" ")]
    for i in range(0, len(seed_line), 2):
        seed_ranges.add((seed_line[i], seed_line[i] + seed_line[i + 1] - 1))
    lines = lines[2:]

    ## Extract each type map
    all_type_maps = []
    for line in lines:
        line = line.replace("\n", "")
        if line.count("map") == 1:
            all_type_maps.append(
                TypeMap(line.split("-")[0], line.split(" ")[0].split("-")[-1], set())
            )
        elif line != "":
            line = [int(n) for n in line.split(" ")]
            all_type_maps[-1].value_maps.add(
                ValueMap(line[1], line[1] + line[2] - 1, line[0], line[0] + line[2] - 1)
            )

    return seed_ranges, tuple(all_type_maps)


if __name__ == "__main__":

    seed_ranges, all_type_maps = import_input()

    for type_map in all_type_maps:
        seed_ranges = apply_type_map_on_ranges(type_map, seed_ranges)

    location_ranges = sorted(list(seed_ranges), key=lambda r: r[0])

    print("Day 5 Part 2:", location_ranges[0][0])
