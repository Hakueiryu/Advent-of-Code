from math import floor

def check_repetition(s):
    if len(s) % 2 != 0: return False
    return s[:len(s)//2] == s[len(s)//2:]


def check_repetition_enhanced(s):

    # Get Divisors
    divisors = set()
    for i in range(1, floor(len(s)**0.5) + 1):
        if len(s) % i == 0:
            divisors.add(i)
            divisors.add(len(s) // i)

    for x in divisors:
        slices = [s[i:i+x] for i in range(0, len(s), x)]
        if len(slices) < 2: continue
        # Check if all slices are equal
        if len(set(slices)) == 1:
            return True
    return False

def part1(line):
    output = 0
    ranges = [tuple(map(int, x.split("-"))) for x in line.split(",")]

    for start, end in ranges:
        for y in range(start, end + 1):
            if check_repetition(str(y)):
                output += y
    return output

def part2(line):
    output = 0
    ranges = [tuple(map(int, x.split("-"))) for x in line.split(",")]

    for start, end in ranges:
        for y in range(start, end + 1):
            if check_repetition_enhanced(str(y)):
                output += y
    return output

if __name__ == '__main__':
    example = open("example1.txt", "r").read().strip().splitlines()[0]
    print(f"Part 1 (Example): {part1(example)}") # Solution: 1227775554
    print(f"Part 2 (Example): {part2(example)}") # Solution: 4174379265

    try:
        input_data = open("input.txt", "r").read().strip().splitlines()[0]
        print(f"Part 1: {part1(input_data)}")
        print(f"Part 2: {part2(input_data)}")
    except FileNotFoundError:
        print("input.txt not found")
