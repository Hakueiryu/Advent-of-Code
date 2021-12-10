from collections import deque

score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closed_to_opened = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

opened_to_closed = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')

    total_scores = []

    for x in file[:]:
        de = deque()
        for c in x:
            if c in closed_to_opened.values():
                de.append(c)
            else:
                if not de.pop() == closed_to_opened[c]:
                    x = None

        if x:
            de = deque()
            personal_score = 0
            for c in x:
                if c == '(' or c == '[' or c == '{' or c == '<':
                    de.append(c)
                else:
                    de.pop()

            while de:
                personal_score = 5*personal_score + score[opened_to_closed[de.pop()]]
            total_scores.append(personal_score)

    total_scores.sort()
    print(f'Part 2: {total_scores[len(total_scores)//2]}')