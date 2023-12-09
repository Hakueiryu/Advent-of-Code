from functools import reduce

def part1(file):
    output = 0
    for line in file:
        nums = [int(x) for x in line.split()]
        last_numbers = []
        while any(x != 0 for x in nums):
            # Save last number
            last_numbers.append(nums[-1])
            # Decrease them all
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        # Cumulative sum
        output += reduce(lambda x,y: x+y, last_numbers)

    print(f'Part 1: {output}')

def part2(file):
    output = 0
    for line in file:
        nums = [int(x) for x in line.split()[::-1]] # Now it's reversed
        last_numbers = []
        while any(x != 0 for x in nums):
            # Save last number
            last_numbers.append(nums[-1])
            # Decrease them all
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        # Cumulative sum
        output += reduce(lambda x,y: x+y, last_numbers)

    print(f'Part 2: {output}')


if __name__ == '__main__':
    file = open("input.txt", 'r').read().strip().splitlines()

    part1(file)
    part2(file)