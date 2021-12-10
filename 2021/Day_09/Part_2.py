from collections import Counter
from operator import mul
from functools import reduce

matrix = []

directions = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
]

# Returns the low point associated to a given point
def get_basin(x,y):
    next = None
    for t in get_adjacent(x,y):
        if matrix[t[0]][t[1]] < matrix[x][y]:
            next = t
    if next is None:
        return (x,y)
    else:
        return get_basin(*next)



def get_adjacent(x,y):
    return [((x+dx), (y+dy)) for dx, dy in directions if 0 <= x+dx <= len(matrix[0]) - 1 and 0 <= y+dy <= len(matrix) - 1]

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    matrix = [list(map(int, list(x))) for x in file]

    basins = []

    # For each point, keep track of its low point
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] != 9:
                basins.append(get_basin(x,y))

    # Multiply the number of occurrences of the top 3 low points
    output = reduce(mul, [x for _, x in Counter(basins).most_common(3)])

    print(f'Part 2: {output}')
