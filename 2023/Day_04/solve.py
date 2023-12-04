
def part1(file):
    output = 0

    for line in file:
        # Parse
        card = line.split(": ")[1]
        winning_numbers, numbers = card.split(" | ")
        winning_numbers = [int(x.strip()) for x in winning_numbers.split()]
        numbers = [int(x.strip()) for x in numbers.split()]
        # count number of wins
        hits = 0
        for num in winning_numbers:
            if num in numbers:
                hits += 1
        output += 2 ** (hits - 1) if hits != 0 else 0

    print(f'Part 1: {output}')

def part2(file):
    card_won = {}

    for line in file:
        # Parse
        id, card = line.split(": ")
        id = int(id.split()[1].strip())
        winning_numbers, numbers = card.split(" | ")
        winning_numbers = [int(x.strip()) for x in winning_numbers.split()]
        numbers = [int(x.strip()) for x in numbers.split()]
        # Count number of wins
        hits = 0
        for num in winning_numbers:
            if num in numbers:
                hits += 1

        # I win the current card by default
        if id not in card_won:
            card_won[id] = 1
        else:
            card_won[id] += 1

        # And also all the following ones based on hits
        for x in range(1,hits+1):
            if x+id not in card_won:
                card_won[x+id] = 1 * card_won[id]
            else:
                card_won[x+id] = card_won[x+id]+ 1 * card_won[id]

    output = sum(card_won.values())
    print(f'Part 2: {output}')

if __name__ == '__main__':
    file = open("input.txt", 'r').read().strip().splitlines()

    part1(file)
    part2(file)