from itertools import permutations

# - Create a hardcoded mapping of letters that represent numbers
# - Create all possible associations of 'abcdefg' with my personal mapping
# 	- Ex. 'a' in the input might mean 'g' in my mapping, so an association would be a --> g
# - Look at the left part of the input and find the association that translates every string to something that is in
#   my mapping
# - Use that association to translate the right part of the input
# - Retrieve the numbers

dictionary = {
    'abcefg' : 0,
    'cf' : 1,
    'acdeg' : 2,
    'acdfg' : 3,
    'bcdf' : 4,
    'abdfg' : 5,
    'abdefg' : 6,
    'acf' : 7,
    'abcdefg' : 8,
    'abcdfg' : 9
}

if __name__ == '__main__':
    input = open('input.txt', 'r').read().strip().split('\n')

    output = 0

    for x in input:
        left, right = x.split(' | ')
        left = left.split()
        right= right.split()

        for permutation in permutations('abcdefg'):
            association = zip(permutation, 'abcdefg')
            mapping = {k:v for k,v in association}
            left_mapping = []
            for l in left:
                t = ''
                for c in l:
                    t += mapping[c]
                left_mapping.append(''.join(sorted(t)))

            if all(l in dictionary for l in left_mapping):
                right_mapping = []
                for r in right:
                    t = ''
                    for c in r:
                        t += mapping[c]
                    right_mapping.append(''.join(sorted(t)))

                output += int(''.join(str(dictionary[r]) for r in right_mapping))

                break

    print(f'Part 2: {output}')

