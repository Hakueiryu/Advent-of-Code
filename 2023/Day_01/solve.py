
def part1(file):
    output = 0
    digits = [''.join(list(filter(lambda x: x.isdigit(), line))) for line in file]

    for x in digits:
        output += int(x[0] + x[-1])

    print(f'Part 1: {output}')

def part2(file):
    output = 0
    english_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five':  '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    parsed_lines = []
    for line in file:
        parsed_line = ''
        cur = ''
        for char in line:
            # If digit keep it as it is
            if char.isdigit():
                parsed_line += char
                continue
            # Progressively add letters and see if it's a word
            cur += char
            for word, number in english_numbers.items():
                if word in cur:
                    parsed_line += number
                    # keep only last letter (to detect overlap)
                    cur = cur[-1]
                    break
        parsed_lines.append(parsed_line)

    # Build output
    for x in parsed_lines:
        output += int(x[0] + x[-1])

    print(f'Part 2: {output}')



if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().splitlines()

    part1(file)
    part2(file)



