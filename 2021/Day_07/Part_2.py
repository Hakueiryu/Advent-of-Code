if __name__ == '__main__':
    input = [int(x) for x in open('input.txt', 'r').read().strip().split(',')]

    output = 1000000000
    for x in range(min(input), max(input) + 1):
        output = min(output, sum(abs(x-y) * (abs(x-y) + 1)//2 for y in input))    # 1+...+n = n(n+1)/2

    print(f'Part 2: {output}')