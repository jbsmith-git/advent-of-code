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


def correct_update_order(rules: set[tuple[int]], update: tuple[int]) -> bool:

    for rule in rules:

        if rule[0] not in update or rule[1] not in update:
            continue

        if update.index(rule[0]) > update.index(rule[1]):
            return False

    return True


def middle_page_number(update: tuple[int]) -> int:

    if len(update) % 2 == 1:
        return update[len(update) // 2]
    else:
        raise Exception("There is no middle!")


if __name__ == "__main__":

    rules, updates = import_input()

    middle_page_number_sum = 0
    for update in updates:
        if correct_update_order(rules, update):
            middle_page_number_sum += middle_page_number(update)

    print("Day 5 Part 1:", middle_page_number_sum)
