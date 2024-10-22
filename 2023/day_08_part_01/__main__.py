from dataclasses import dataclass


@dataclass
class Node:
    label: str
    left: str
    right: str


def import_input() -> tuple[list[str], list[Node]]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    lr_instructions = list(lines[0].replace("\n", ""))

    all_nodes = []
    for line in lines[2:]:
        line = line.replace(")", "").replace("\n", "")
        line = line.replace(" = (", ".").replace(", ", ".")
        line = line.split(".")
        all_nodes.append(Node(*line))

    return lr_instructions, all_nodes


def solve_network(lr_instructions, all_nodes):

    node_label_map = {node.label: node for node in all_nodes}

    node_steps = 0
    active_node_label = "AAA"
    while True:
        for i in lr_instructions:
            node = node_label_map[active_node_label]
            if i == "L":
                active_node_label = node.left
            else:
                active_node_label = node.right
            node_steps += 1
            if active_node_label == "ZZZ":
                return node_steps


if __name__ == "__main__":

    lr_instructions, all_nodes = import_input()

    node_steps = solve_network(lr_instructions, all_nodes)

    print("Day 8 Part 1:", node_steps)
