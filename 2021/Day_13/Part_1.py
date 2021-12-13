matrix = set()

def fold_x(x):
    for p in set(matrix):
        if p[0] > x:
            matrix.remove(p)
            matrix.add((x - (p[0] - x), p[1]))

def fold_y(y):
    for p in set(matrix):
        if p[1] > y:
            matrix.remove(p)
            matrix.add((p[0], y - (p[1] - y)))


if __name__ == '__main__':
    coordinates, folds = open('input.txt', 'r').read().strip().split('\n\n')

    # Parse points
    for x in coordinates.split('\n'):
        a, b = x.split(',')
        matrix.add((int(a), int(b)))

    # Parse fold
    first_fold = folds.split('\n')[0]
    axis, amount = first_fold.split('=')
    amount = int(amount)
    axis = axis[-1]

    if axis == 'x':
        fold_x(amount)
    if axis == 'y':
        fold_y(amount)

    print(f'Part 1: {len(matrix)}')