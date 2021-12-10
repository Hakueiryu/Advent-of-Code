
if __name__ == '__main__':

    file = open('input.txt', 'r')
    measurements = [int(x) for x in file.read().strip().split('\n')]

    output = 0
    for x in range(len(measurements) - 1):
        if measurements[x] < measurements[x+1]:
            output += 1

    print(f'Part 1: {output}')
