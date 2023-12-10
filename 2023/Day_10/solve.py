
directions = {
    'R': (0,1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}

pipes = {
    '-': ['L', 'R'],
    '|': ['U', 'D'],
    'L': ['U', 'R'],
    '7': ['D', 'L'],
    'F': ['D', 'R'],
    'J': ['U', 'L'],
    'S': ['U', 'D', 'L', 'R']
}

def get_directions(pipe_type):
    return [directions[x] for x in pipes[pipe_type]]

def get_neighbors(x,y, grid):
    neighbors = [(x+dx, y+dy) for dx,dy in get_directions(grid[x][y])
            if 0 <= x+dx <= len(grid) -1
            and 0 <= y+dy <= len(grid[0]) -1
            and grid[x+dx][y+dy] in pipes]
    return neighbors

def get_valid_neighbors(x,y,grid):
    # A neighbor is valid if it is itself a neighbor of its neighbor
    # L and - are valid neighbors horizontally
    # J and | are not valid neighbors horizontally
    neighbors = get_neighbors(x,y,grid)
    valid_neighbors = [p for p in neighbors if (x,y) in get_neighbors(*p, grid)]
    return valid_neighbors

def traverse(root: tuple[int, int], grid, visited):

    stack = [root]
    while stack:
        current_node = stack.pop()
        visited.append(current_node)

        neighbors = get_valid_neighbors(*current_node, grid)
        unvisited_neighbors = [x for x in neighbors if x not in visited and x not in stack]
        stack.extend(unvisited_neighbors)

    return visited

def area(points):
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        determinant = (x1 * y2) - (x2 * y1)
        area += determinant
    return abs(area) // 2


def part1(file):
    starting_coordinate = None
    # look for starting point
    for i,line in enumerate(file):
        for j, char in enumerate(line):
            if char == 'S': starting_coordinate = (i,j)

    path = traverse(starting_coordinate, file, [])
    output = len(path) // 2
    print(f'Part 1: {output}')



def part2(file):
    #  Step 1: Area = 1/2 {sum (i = 1, ... n) [det((xi yi), (xi+1 yi+1)]}
    #  Step 2: Area = Inside_Points + N_Boundary_Points/2 - 1
    #          --> Inside_Points = Area - N_Boundary_Points/2 + 1

    starting_coordinate = None
    # look for starting point
    for i,line in enumerate(file):
        for j, char in enumerate(line):
            if char == 'S': starting_coordinate = (i,j)

    path = traverse(starting_coordinate, file, [])

    output = area(path) - len(path) // 2 + 1
    print(f'Part 2: {output}')

if __name__ == '__main__':
    file = open("input.txt", "r").read().strip().splitlines()

    part1(file)
    part2(file)