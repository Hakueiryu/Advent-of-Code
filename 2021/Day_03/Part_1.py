
gamma = ''
epsilon = ''

# Input: dictionary with, for each key, the number of occurrences of 0s and 1s
# Outputs a string str such that
# str[x] = 0 if 0 is the most common bit in position 0
# str[x] = 1 if 1 is the most common bit in position 1
def most_bits(dictionary):
    output = ''
    for x in list(dictionary.keys()):
        val = dictionary.get(x)
        if val[0] > val[1]:
            output += '0'
        else:
            output += '1'
    return output

# Input: dictionary with, for each key, the number of occurrences of 0s and 1s
# Outputs a string str such that
# str[x] = 0 if 0 is the least common bit in position 0
# str[x] = 1 if 1 is the least common bit in position 1
def least_bits(dictionary):
    output = ''
    for x in list(dictionary.keys()):
        val = dictionary.get(x)
        if val[0] <= val[1]:
            output += '0'
        else:
            output += '1'
    return output

# Input: list of binary strings
# Output: dictionary {k,v} such that
# - k corresponds to a bit position
# - v is a tuple (a,b) such that
# - - a is the number of occurrences of bit '0' in position k considering all the strings
# - - b is the number of occurrences of bit '1' in position k considering all the strings
def parse_dictionary(input):
    dictionary = {}

    for x in input:
        for y in range(len(x)):
            if y not in dictionary:
                dictionary[y] = [0, 0]
            val = dictionary.get(y)
            if x[y] == '0':
                val[0] += 1
            if x[y] == '1':
                val[1] += 1
            dictionary.update({y: val})
    return dictionary

def main():
    global gamma
    global epsilon

    file = open('input.txt', 'r').read().strip().split('\n')    # Parse input

    dictionary = parse_dictionary(file)

    gamma = most_bits(dictionary)
    epsilon = least_bits(dictionary)


if __name__ == '__main__':

    main()
    gamma_rate = int(gamma, 2)
    epsilon_rate = int(epsilon, 2)
    print(f'Part 1: {gamma_rate * epsilon_rate}')

