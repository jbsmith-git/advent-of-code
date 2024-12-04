def import_input() -> str:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    ## There aren't any "\n" in the input
    memory = "-".join((line.replace("\n", "") for line in lines))

    return memory


def sum_all_mults(memory: str) -> int:

    mult_sum = 0
    mult_enabled = True
    for i in range(0, len(memory) - 7):

        ## Search for mul(
        if mult_enabled and memory[i : i + 4] == "mul(":

            ## Check for number and ,
            num_1, j = [], i + 4
            while memory[j] in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                num_1.append(memory[j])
                j += 1
            if len(num_1) == 0 or memory[j] != ",":
                continue

            ## Check for number and )
            num_2, j = [], j + 1
            while memory[j] in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                num_2.append(memory[j])
                j += 1
            if len(num_2) == 0 or memory[j] != ")":
                continue

            mult_sum += int("".join(num_1)) * int("".join(num_2))

        ## Search for do()
        elif memory[i : i + 4] == "do()":
            mult_enabled = True

        ## Search for don't()
        elif memory[i : i + 7] == "don't()":
            mult_enabled = False

    return mult_sum


if __name__ == "__main__":

    memory = import_input()

    total_mult_sum = sum_all_mults(memory)

    print("Day 3 Part 2:", total_mult_sum)
