def total_paths(x_min, x_max, y_min, y_max):
    output = 0
    for v0_x in range(1, x_max + 1):
        for v0_y in range(y_min, -y_min):
            x, y = 0, 0
            v_x, v_y = v0_x, v0_y

            while x <= x_max and y >= y_min:
                if x >= x_min and y <= y_max:
                    output += 1
                    break
                x, y = (x+v_x, y+v_y)
                v_y -= 1
                if v_x > 0:
                    v_x -= 1
    return output

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip()

    x,y = [x.split('=')[1].split('..') for x in file.split(':')[1].split(',')]

    x_min, x_max = list(map(int, x))
    y_min, y_max = list(map(int, y))

    output = total_paths(x_min, x_max, y_min, y_max)
    print(f'Part 2: {output}')


