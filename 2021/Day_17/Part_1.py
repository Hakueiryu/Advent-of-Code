if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip()

    x,y = [x.split('=')[1].split('..') for x in file.split(':')[1].split(',')]

    x_min, x_max = list(map(int, x))
    y_min, y_max = list(map(int, y))

    output = (abs(y_min) - 1) * abs(y_min) // 2

    print(f'Part 1: {output}')
