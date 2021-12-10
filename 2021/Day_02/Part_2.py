
depth = 0
horizontal = 0
aim = 0

# Gets the direction and value, and applies the rules (see text description)
def parse_command(command):
    global horizontal
    global depth
    global aim

    dir, value = command[0], int(command[1])
    if dir == 'forward':
        horizontal += value
        depth += aim * value
    if dir == 'down':
        aim += value
    if dir == 'up':
        aim -= value



if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')    # Parse input

    for x in file:
        parse_command(x.split(' '))

    print(f'Part 2: {depth * horizontal}')                      # Print output