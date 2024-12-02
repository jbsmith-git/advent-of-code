from dataclasses import dataclass
import itertools as it
import math


@dataclass
class Node:
    label: str
    left: str
    right: str
    z_cycle: list[tuple[str, int]] = None


def import_input() -> tuple[tuple[str], dict[str, Node]]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    lr_instructions = tuple(lines[0].replace("\n", ""))

    all_nodes = {}
    for line in lines[2:]:
        label, left, right = line[:3], line[7:10], line[12:15]
        all_nodes[label] = Node(label, left, right)

    return lr_instructions, all_nodes


def compute_z_cycles(lr_instructions: tuple[str], all_nodes: dict[str, Node]) -> None:

    for node in all_nodes.values():

        if node.label[2] not in {"A", "Z"}:
            continue

        node.z_cycle = [(node.label, 0)]

        active_node = node
        steps = 0
        for i in it.cycle(lr_instructions):

            if i == "L":
                active_node = all_nodes[active_node.left]
            else:
                active_node = all_nodes[active_node.right]
            steps += 1

            if active_node.label[2] == "Z":
                node.z_cycle.append((active_node.label, steps))

                if [c[0] for c in node.z_cycle].count(active_node.label) == 2:
                    break


if __name__ == "__main__":

    lr_instructions, all_nodes = import_input()

    compute_z_cycles(lr_instructions, all_nodes)

    ## The z_cycles all only hit a single Z node!
    start_nodes = [node for node in all_nodes.values() if node.label[2] == "A"]
    steps_to_all_z = math.lcm(*[node.z_cycle[1][1] - node.z_cycle[0][1] for node in start_nodes])

    print("Day 8 Part 2:", steps_to_all_z)
