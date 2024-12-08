import random


def import_input() -> tuple[set[tuple[int]], set[tuple[int]]]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    rules = set()
    updates = set()
    for line in lines:
        line = line.replace("\n", "")
        if len(line) == 5:
            rules.add((int(line[:2]), int(line[3:5])))
        elif len(line) > 5:
            updates.add(tuple(int(p) for p in line.split(",")))

    return rules, updates


def count_rules_disobeyed(rules: set[tuple[int]], update: tuple[int]) -> int:

    rules_disobeyed = 0
    for rule in rules:

        if rule[0] not in update or rule[1] not in update:
            continue

        if update.index(rule[0]) > update.index(rule[1]):
            rules_disobeyed += 1

    return rules_disobeyed


def middle_page_number(update: tuple[int]) -> int:

    if len(update) % 2 == 1:
        return update[len(update) // 2]
    else:
        raise Exception("There is no middle!")


def correct_update(rules: set[tuple[int]], update: tuple[int]) -> tuple[int]:

    update_indices = [i for i in range(len(update))]
    update = list(update)

    while True:

        pre_swap_rules_disobeyed = count_rules_disobeyed(rules, update)
        swap = random.sample(update_indices, 2)
        update[swap[0]], update[swap[1]] = update[swap[1]], update[swap[0]]
        post_swap_rules_disobeyed = count_rules_disobeyed(rules, update)

        if post_swap_rules_disobeyed == 0:
            return tuple(update)

        if post_swap_rules_disobeyed > pre_swap_rules_disobeyed:
            update[swap[0]], update[swap[1]] = update[swap[1]], update[swap[0]]


if __name__ == "__main__":

    rules, updates = import_input()

    middle_page_number_sum = 0
    for update in updates:
        if count_rules_disobeyed(rules, update) != 0:
            corrected_update = correct_update(rules, update)
            middle_page_number_sum += middle_page_number(corrected_update)

    print("Day 5 Part 2:", middle_page_number_sum)
