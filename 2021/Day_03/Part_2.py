import Part_1

oxygen_generator_rating = 0
co2_scrubber_rating = 0

# Input: bit criteria, list of binary strings
# Output: The last string that, iteratively, matches the bit criteria
def bit_filter(fun, input):
    x = 0
    while len(input) != 1:
        t = fun(Part_1.parse_dictionary(input))
        for num in input[:]:
            if num[x] != t[x]:
                input.remove(num)
        x += 1
    return input[0]

if __name__ == '__main__':
    Part_1.main()

    file1 = open('input.txt', 'r').read().strip().split('\n')  # Parse input
    file2 = open('input.txt', 'r').read().strip().split('\n')  # Parse input

    oxygen_generator_rating = bit_filter(Part_1.most_bits, file1)
    co2_scrubber_rating = bit_filter(Part_1.least_bits, file2)

    print(f'Part 2: {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}')