
matrix = []

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def get_adjacent(x,y):
    return [((x+dx), (y+dy)) for dx, dy in directions if 0 <= x+dx <= len(matrix[0]) - 1 and 0 <= y+dy <= len(matrix) - 1]


if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    matrix = [list(map(int, list(x))) for x in file]

    output = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if all(matrix[a[0]][a[1]] > matrix[x][y] for a in get_adjacent(x,y)):
                output += matrix[x][y] + 1

    print(f'Part 1: {output}')



