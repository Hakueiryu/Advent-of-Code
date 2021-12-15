from collections import defaultdict

matrix = []

directions = [
    (0,-1),
    (0,1),
    (-1,0),
    (1,0)
]

def get_cost(x,y):
    return matrix[x][y]

def get_adjacent(x,y):
    return [((x+dx), (y+dy)) for dx,dy in directions if 0 <= x+dx <= len(matrix[0]) - 1 and 0 <= y+dy <= len(matrix) - 1]

def expand_matrix(matrix):
    expanded_m = [[0 for _ in range(5 * len(matrix))] for _ in range(5 * len(matrix))]

    for x in range(len(expanded_m)):
        for y in range(len(expanded_m[0])):
            distance = x // len(matrix) + y // len(matrix[0])
            new_value = matrix[x % len(matrix)][y % len(matrix[0])] # The original value to increase
            for _ in range(distance):
                new_value += 1
                if new_value == 10:
                    new_value = 1
            expanded_m[x][y] = new_value

    return expanded_m

def uniform_cost_search(start, goal):
    seen = set()
    queue = defaultdict(list)
    queue[0].append(start)

    while queue:
        x = min(list(queue.keys()))
        cost, node = x, queue[x].pop()
        if not queue[x]:
            del queue[x]
        if node not in seen:
            seen.add(node)
            if node == goal:
                return cost
            for s in get_adjacent(*node):
                if s not in seen:
                    total_cost = cost + get_cost(*s)
                    queue[total_cost].append(s)

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    base_matrix = [list(map(int, x)) for x in file]

    matrix = expand_matrix(base_matrix)

    start = (0,0)
    goal = (len(matrix) - 1, len(matrix) - 1)
    total_cost = uniform_cost_search(start, goal)

    print(f'Part 2: {total_cost}')
