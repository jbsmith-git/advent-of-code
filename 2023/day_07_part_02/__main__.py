class Hand:

    def __init__(self, cards: list[str], bid: int):

        card_conversions = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
        cards = [card_conversions.get(card, card) for card in cards]
        self.cards = [int(card) for card in cards]
        self.bid = bid

        joker_count = self.cards.count(1)

        unique_cards = set(self.cards)
        if 1 in unique_cards:
            unique_cards.remove(1)

        card_counts = [self.cards.count(u) for u in unique_cards]
        card_counts.sort(reverse=True)

        ## Check length in case we have 5 jokers
        if len(card_counts) > 0:
            card_counts[0] += joker_count
        else:
            card_counts = [5]

        card_counts = [str(c) for c in card_counts]
        card_counts = "".join(card_counts)
        card_counts_type_map = {"5": 7, "41": 6, "32": 5, "311": 4, "221": 3, "2111": 2, "11111": 1}
        self.type = card_counts_type_map.get(card_counts)

        self.ordering = (self.type, *self.cards)


def import_input() -> list[Hand]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    all_hands = []
    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        all_hands.append(Hand(list(line[0]), int(line[1])))

    return all_hands


if __name__ == "__main__":

    all_hands = import_input()

    all_hands.sort(key=lambda h: h.ordering)

    total_winnings = 0
    for h in range(len(all_hands)):
        total_winnings += all_hands[h].bid * (h + 1)

    print("Day 7 Part 2:", total_winnings)
