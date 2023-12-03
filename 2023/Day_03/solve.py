from functools import reduce

directions = [
    (0,1),
    (0,-1),
    (1,0),
    (1,1),
    (1,-1),
    (-1,0),
    (-1,1),
    (-1,-1)
]

def get_neighbors_of_a_point(x,y, grid):
    return [(x+dx, y+dy) for dx,dy in directions if 0 <= x+dx <= len(grid) -1 and 0 <= y+dy <= len(grid[0]) -1]

def get_neighbors_of_a_set_of_points(points, grid):
    neighbors = set()
    for point in points:
        ## Add only points that are not part of the points list
        for neighbor in get_neighbors_of_a_point(point[0], point[1], grid):
            if neighbor not in points:
                neighbors.add(neighbor)
    return neighbors

def process_number(number, points, grid):
    neighbors = get_neighbors_of_a_set_of_points(points, grid)
    if any(not grid[x[0]][x[1]].isdigit() and grid[x[0]][x[1]] != '.' for x in neighbors):
        return int(number)
    else:
        return 0

def check_if_in_gear_range_and_update(number, points, grid, gears):
    neighbors = get_neighbors_of_a_set_of_points(points, grid)
    for neighbor in neighbors:
        if grid[neighbor[0]][neighbor[1]] == '*':
            # Associate gear coordinate to number
            if neighbor not in gears:
                gears[neighbor] = [int(number)]
            else:
                gears[neighbor].append(int(number))

def part1(file):
    output = 0
    for i, line in enumerate(file):
        # Scan the line and get the numbers
        number = ''
        points = []
        for j, char in enumerate(line):
            if char.isdigit():
                number += char
                points.append((i,j))
                if j == len(line) - 1:
                    # We have reached the end of the line
                    output += process_number(number, points, file)
            else:
                if number:
                    # We have finished a number sequence
                    output += process_number(number, points, file)
                    number = ''
                    points = []


    print(f'Part 1: {output}')

def part2(file):
    output = 0
    gears = {}
    for i, line in enumerate(file):
        # Scan the line and get the numbers
        number = ''
        points = []
        for j, char in enumerate(line):
            if char.isdigit():
                number += char
                points.append((i,j))
                if j == len(line) - 1:
                    # We have reached the end of the line
                    check_if_in_gear_range_and_update(number, points, file, gears)
            else:
                if number:
                    # We have finished a number sequence
                    check_if_in_gear_range_and_update(number, points, file, gears)
                    number = ''
                    points = []

    output = sum([reduce(lambda x,y: x*y, gears[point]) for point in gears.keys() if len(gears[point]) == 2])
    print(f'Part 2: {output}')



if __name__ == '__main__':
    file = open("input.txt", 'r').read().strip().splitlines()

    part1(file)
    part2(file)