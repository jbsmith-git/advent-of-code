import functools as functools


def import_input() -> dict[int, int]:

    with open("input.txt", "r") as input_file:
        line = input_file.readlines()[0]

    ## Order of stones doesn't actually matter
    ## There are no duplicates in the initial input
    all_stones = {int(s): 1 for s in line.replace("\n", "").split(" ")}

    return all_stones


@functools.cache
def apply_blink_to_single_stone(stone: int) -> tuple[int]:

    if stone == 0:
        return (1,)

    elif len(str(stone)) % 2 == 0:
        stone_length = len(str(stone))
        left_stone = int(str(stone)[: stone_length // 2])
        right_stone = int(str(stone)[stone_length // 2 :])
        return (left_stone, right_stone)

    return (stone * 2024,)


def apply_blink_to_all_stones(all_stones: dict[int, int]) -> dict[int, int]:

    all_stones_after_blink = {}
    for stone, count in all_stones.items():

        stones_after_blink = apply_blink_to_single_stone(stone)
        for stone_ab in stones_after_blink:

            if stone_ab not in all_stones_after_blink.keys():
                all_stones_after_blink[stone_ab] = count
            else:
                all_stones_after_blink[stone_ab] += count

    return all_stones_after_blink


if __name__ == "__main__":

    all_stones = import_input()

    for _ in range(75):
        all_stones = apply_blink_to_all_stones(all_stones)

    print("Day 11 Part 2:", sum(all_stones.values()))
