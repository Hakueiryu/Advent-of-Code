from Part_1 import parse_string
from Part_1 import node
from Part_1 import sum_expressions

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    output = 0

    for x in file:
        for y in file:
            a = parse_string(node(), eval(x))
            b = parse_string(node(), eval(y))
            c1 = sum_expressions(a,b).magnitude()
            output = max(c1, output)

    print(f'Part 2: {output}')