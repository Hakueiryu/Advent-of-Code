if __name__ == '__main__':
    input = [int(x) for x in open('input.txt', 'r').read().strip().split(',')]

    output = 1000000000
    for x in range(min(input), max(input) + 1):
        output = min(output, sum(abs(x-y) for y in input))

    print(f'Part 1: {output}')
