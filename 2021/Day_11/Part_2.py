matrix = []
flashed = []
synchronized_flashes = 0

directions = [
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1)
]

def get_adjacent(x,y):
    return [((x+dx), (y+dy)) for dx, dy in directions if 0 <= x+dx <= len(matrix[0]) - 1 and 0 <= y+dy <= len(matrix) - 1]

def simulate_step():
    global matrix
    global flashed
    global synchronized_flashes

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            increase_step(x,y)

    if all(flashed[x][y] for x in range(len(flashed[x])) for y in range(len(flashed))):
        synchronized_flashes += 1

def increase_step(x,y):
    global synchronized_flashes
    global matrix
    global flashed

    if not flashed[x][y]:
        matrix[x][y] += 1
        if matrix[x][y] > 9:
            matrix[x][y] = 0
            flashed[x][y] = 1
            for a, b in get_adjacent(x, y):
                increase_step(a, b)


if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    matrix = [list(map(int, list(x))) for x in file]

    output = 0
    while synchronized_flashes != 1:
        flashed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(len(matrix))]
        simulate_step()
        output += 1

    print(f'Part 2: {output}')