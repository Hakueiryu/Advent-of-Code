if __name__ == '__main__':
    input = [int(x) for x in open('input.txt', 'r').read().strip().split(',')]

    population = [0,0,0,0,0,0,0,0,0]        # Population[x] = the number of fish that will give birth in x days
    for x in input:
        population[x] += 1

    for _ in range(256):
        gave_birth = population.pop(0)      # Get the number of fish that are giving birth now.
        population[6] += gave_birth         # Add this number to the number of fish that are giving birth in 7 days
        population.append(gave_birth)       # Add this number to the end of the list (fish that will give birth in 9 days)

    print(f'Part 2: {sum(population)}')
