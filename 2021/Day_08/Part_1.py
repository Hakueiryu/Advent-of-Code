
def decode_unique_digit(output):
    result = 0
    for x in output.split():
        l = len(x)
        if l == 2 or l == 4 or l == 3 or l == 7:
            result += 1
    return result


if __name__ == '__main__':
    input = open('input.txt', 'r').read().strip().split('\n')
    input = [x.split(' | ')[1] for x in input]

    output = 0
    for x in input:
        output += decode_unique_digit(x)

    print(f'Part 1: {output}')