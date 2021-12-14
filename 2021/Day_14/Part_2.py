from collections import Counter

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n\n')

    starting_string = file[0]
    rules = file[1]

rules = { rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in rules.split("\n") }

pairs = zip(starting_string, starting_string[1:])
pairs = Counter( (c1+c2) for c1, c2 in pairs )          # cx = character x

for _ in range(40):
    next_pairs = Counter()

    for pair, num in pairs.items():
        c1, c2 = pair
        t = rules[pair]
        next_pairs[c1+t] += num
        next_pairs[t+c2] += num

    pairs = next_pairs

total_counter = Counter()
for pair, num in pairs.items():
    # If i take the first character of each pair, i get all the characters that would be in the current string
    # NOTE: This way i would skip one occurrence of the last character in the first string
    total_counter[pair[0]] += num
total_counter[starting_string[-1]] += 1 # Fix the missing occurrence

print(total_counter.most_common()[0][1] - total_counter.most_common()[-1][1])