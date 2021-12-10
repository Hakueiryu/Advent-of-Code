from collections import defaultdict

plain = defaultdict(int)

def update_dictionary(start, end):
    global plain

    x1, y1 = [int(x) for x in start.split(',')]
    x2, y2 = [int(x) for x in end.split(',')]

    if(x1 == x2 or y1 == y2):
        dx = ((x2 - x1) // abs(x2 - x1)) if (x2 - x1) != 0 else 0   # +1, -1 or 0
        dy = ((y2 - y1) // abs(y2 - y1)) if (y2 - y1) != 0 else 0   # +1, -1 or 0

        a = x1
        b = y1
        plain[(a, b)] += 1
        while not(a == x2 and b == y2):     # keep adding points until you reach the end
            a += dx
            b += dy
            plain[(a, b)] += 1


if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')

    for x in file:
        start, end = x.split(' -> ')
        update_dictionary(start, end)

    output = len([x for x in plain.values() if x > 1])
    print(f'Part 1: {output}')
