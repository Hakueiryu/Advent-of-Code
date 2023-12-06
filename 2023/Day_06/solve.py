from functools import reduce

def part1(file):
    times = [int(x.strip()) for x in file[0].split(":")[1].split()]
    record_distances = [int(x.strip()) for x in file[1].split(":")[1].split()]
    wins = []
    for i in range(len(times)):
        win = 0
        for v in range(times[i]):
            distance = v * (times[i] - v)
            if distance > record_distances[i]:
                win += 1
        wins.append(win)

    output = reduce(lambda x,y: x*y, wins)
    print(f'Part 1: {output}')

def part2(file):
    time = int("".join([x.strip() for x in file[0].split(":")[1].split()]))
    record_distance = int("".join([x.strip() for x in file[1].split(":")[1].split()]))
    output = 0
    for v in range(time):
        distance = v * (time - v)
        if distance > record_distance:
            output += 1

    print(f'Part 2: {output}')


if __name__ == '__main__':
    file = open("input.txt").read().strip().splitlines()

    part1(file)
    part2(file)