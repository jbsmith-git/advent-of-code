def import_input() -> list[int]:

    with open("input.txt", "r") as input_file:
        line = input_file.readlines()[0]

    stones = [int(s) for s in line.replace("\n", "").split(" ")]

    return stones


def apply_blink(stones: list[int]) -> list[int]:

    stones_after_blink = []
    for stone in stones:

        if stone == 0:
            stones_after_blink.append(1)

        elif len(str(stone)) % 2 == 0:
            stone_length = len(str(stone))
            left_stone = int(str(stone)[: stone_length // 2])
            right_stone = int(str(stone)[stone_length // 2 :])
            stones_after_blink.extend((left_stone, right_stone))

        else:
            stones_after_blink.append(stone * 2024)

    return stones_after_blink


if __name__ == "__main__":

    stones = import_input()

    for _ in range(25):
        stones = apply_blink(stones)

    print("Day 11 Part 1:", len(stones))
