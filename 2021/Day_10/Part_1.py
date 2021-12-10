from collections import deque

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

closed_to_opened = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')

    error_score = 0

    for x in file:
        de = deque()
        for c in x:
            if c in closed_to_opened.values():
                de.append(c)
            else:
                if not de.pop() == closed_to_opened[c]:
                    error_score += score[c]

    print(f'Part 1: {error_score}')