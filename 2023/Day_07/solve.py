from functools import cmp_to_key
from itertools import product

card_strengths = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
}

card_strengths_with_joker = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

def rank_hand(cards):
    if len(cards) != 5:
        raise Exception("Card length has to be 5")
    card_frequencies = {}
    for card in cards:
        if card not in card_frequencies:
            card_frequencies[card] = 1
        else:
            card_frequencies[card] += 1

    card_set = card_frequencies.keys()

    if len(card_set) == 1: return 7 # Five of a kind
    if len(card_set) == 2 and any(card_frequencies[card] == 4 for card in card_set): return 6 # Four of a kind
    if len(card_set) == 2 and any(card_frequencies[card] == 3 for card in card_set): return 5 # Full house
    if len(card_set) == 3 and any(card_frequencies[card] == 3 for card in card_set): return 4 # Three of a kind
    if len(card_set) == 3 and any(card_frequencies[card] == 2 for card in card_set) and any(card_frequencies[card] == 1 for card in card_set): return 3 # Two pair
    if len(card_set) == 4: return 2 # One pair
    if len(card_set) == 5: return 1 # High Card

def rank_hand_with_joker(cards):
    rank = rank_hand(cards)
    if 'J' not in cards:
        return rank
    else:
        # Extract all indices
        jokers = []
        max_rank = rank
        for i, card in enumerate(cards):
            if card == 'J':
                jokers.append(i)

        possible_substitutions = list(product(card_strengths_with_joker.keys(), repeat=len(jokers)))
        # All possible substitutions of Jokers
        for substitution in possible_substitutions:
            new_hand = list(cards)
            for i, index in enumerate(jokers):
                new_hand[index] = substitution[i]
            max_rank = max(max_rank, rank_hand("".join(new_hand)))

        return max_rank


def compare_hands_by_single_cards(hand1, hand2, withJoker=False):
    # Find first diff
    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:

            card_strength_hand1 = card_strengths[hand1[i]] if not withJoker else card_strengths_with_joker[hand1[i]]
            card_strength_hand2 = card_strengths[hand2[i]] if not withJoker else card_strengths_with_joker[hand2[i]]

            return card_strength_hand1 - card_strength_hand2

    raise Exception("The hands should be different")

def compare_hands(line1, line2, withJoker=False):
    hand1 = line1.split()[0]
    hand2 = line2.split()[0]

    rank_hand_1 = rank_hand(hand1) if not withJoker else rank_hand_with_joker(hand1)
    rank_hand_2 = rank_hand(hand2) if not withJoker else rank_hand_with_joker(hand2)

    if rank_hand_1 != rank_hand_2:
        return rank_hand_1 - rank_hand_2
    else:
        return compare_hands_by_single_cards(hand1, hand2, withJoker)

def part1(file):

    output = 0
    ranked_hands = sorted(file, key=cmp_to_key(lambda x,y: compare_hands(x,y)))
    for i, hand in enumerate(ranked_hands):
        output += (i+1) * int(hand.split()[1])

    print(f'Part 1: {output}')

def part2(file):

    output = 0
    ranked_hands = sorted(file, key=cmp_to_key(lambda x,y: compare_hands(x,y, withJoker=True)))
    for i, hand in enumerate(ranked_hands):
        output += (i+1) * int(hand.split()[1])

    print(f'Part 2: {output}')

if __name__ == '__main__':
    file = open("input.txt", "r").read().strip().splitlines()

    part1(file)
    part2(file)