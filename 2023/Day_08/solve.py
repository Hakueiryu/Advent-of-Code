import math
import re
from itertools import cycle

def part1(file):
    directions = file[0]
    nodes = {}
    for line in file[2:]:
        source, left, right = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)[0]
        nodes[source] = (left, right)

    output = traverse_path("AAA", directions, nodes)

    print(f'Part 1: {output}')

def part2(file):
    directions = file[0]
    nodes = {}
    for line in file[2:]:
        source, left, right = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', line)[0]
        nodes[source] = (left, right)

    # Get all Sources
    sources = []
    for node in nodes.keys():
        if node[-1] == 'A':
            sources.append(node)

    distances = []
    for source in sources:
        distance = traverse_path(source, directions, nodes)
        distances.append(distance)

    output = math.lcm(*distances)
    print(f'Part 2: {output}')

def traverse_path(source, directions, nodes):
    current = source
    distance = 0
    for direction in cycle(directions):
        if direction == 'L': current = nodes[current][0]
        else: current = nodes[current][1]
        distance += 1
        if current[-1] == 'Z': break
    return distance

if __name__ == '__main__':
    file = open("input.txt", "r").read().strip().splitlines()

    part1(file)
    part2(file)