from functools import reduce

def part1(file):
    output = 0
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    for line in file:
        # Parse gameId and rounds
        gameId, rounds = line.split(":")
        gameId = int(gameId.split()[1])
        rounds = rounds.split(";")
        possible = True
        for round in rounds:
            # Divide each extraction of a round
            outcomes = [x.strip() for x in round.split(",")]
            for outcome in outcomes:
                n, color = outcome.split()
                if int(n) > bag[color]:
                    possible = False
        if possible:
            output += gameId


    print(f'Part 1: {output}')

def part2(file):
    output = 0
    for line in file:
        bag = {}
        # Parse gameId and rounds
        gameId, rounds = line.split(":")
        gameId = int(gameId.split()[1])
        rounds = rounds.split(";")
        possible = True
        for round in rounds:
            # Divide each extraction of a round
            outcomes = [x.strip() for x in round.split(",")]
            for outcome in outcomes:
                n, color = outcome.split()
                if color not in bag:
                    bag[color] = int(n)
                else:
                    bag[color] = max(bag[color], int(n))
        output += reduce(lambda x,y: x*y, bag.values())


    print(f'Part 2: {output}')


if __name__ == '__main__':
    file = open("input.txt", 'r').read().strip().splitlines()

    part1(file)
    part2(file)
