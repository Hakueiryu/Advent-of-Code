from numbers import Number

def part1(file) -> Number:
    pos: int = 50
    output: int = 0
    for line in file:
        direction, distance = line[0], int(line[1:])
        if direction == "R":
            pos += distance
        if direction == "L":
            pos -= distance

        if pos % 100 == 0:
            output += 1
    return output

def part2(file) -> Number:
    pos: int = 50
    output: int = 0
    for line in file:
        direction, distance = line[0], int(line[1:])
        prev = pos
        if direction == "R":
            pos += distance
            output += pos // 100 - prev // 100
        if direction == "L":
            pos -= distance
            output += (prev - 1) // 100 - (pos - 1) // 100
    return output

if __name__ == '__main__':
    example = open("example1.txt", "r").read().strip().splitlines()
    # print(f"Part 1 (Example): {part1(example)}")
    # print(f"Part 2 (Example): {part2(example)}")

    try:
        input_data = open("input.txt", "r").read().strip().splitlines()
        print(f"Part 1: {part1(input_data)}")
        print(f"Part 2: {part2(input_data)}")
    except FileNotFoundError:
        print("input.txt not found")
