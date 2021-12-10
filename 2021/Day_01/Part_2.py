
if __name__ == '__main__':

    file = open('input.txt', 'r')
    measurements = [int(x) for x in file.read().strip().split('\n')]

    output = 0
    for x in range(len(measurements) - 3):
        if sum(measurements[x : x+3]) < sum(measurements[x+1 : x+4]):
            output += 1

    print(f'Part 2: {output}')

