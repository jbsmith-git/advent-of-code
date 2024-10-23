from dataclasses import dataclass


@dataclass
class Sequence:
    original: tuple[int]


def import_input() -> tuple[Sequence]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    all_sequences = []
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        line = tuple([int(n) for n in line])
        all_sequences.append(Sequence(line))

    return tuple(all_sequences)


def compute_sequence_diffs(sequence: Sequence):
    sequence.diffs = [
        tuple(
            [
                sequence.original[n] - sequence.original[n - 1]
                for n in range(1, len(sequence.original))
            ]
        )
    ]
    while set(sequence.diffs[-1]) != {0}:
        sequence.diffs.append(
            tuple(
                [
                    sequence.diffs[-1][n] - sequence.diffs[-1][n - 1]
                    for n in range(1, len(sequence.diffs[-1]))
                ]
            )
        )
    sequence.diffs = tuple(sequence.diffs)


def compute_prev_original_term(sequence: Sequence):
    prev_diff_term = 0
    for d in range(len(sequence.diffs) - 2, -1, -1):
        prev_diff_term = sequence.diffs[d][0] - prev_diff_term
    sequence.prev_original_term = sequence.original[0] - prev_diff_term


if __name__ == "__main__":

    all_sequences = import_input()

    prev_original_term_sum = 0
    for s in all_sequences:
        compute_sequence_diffs(s)
        compute_prev_original_term(s)
        prev_original_term_sum += s.prev_original_term

    print("Day 9 Part 2:", prev_original_term_sum)
