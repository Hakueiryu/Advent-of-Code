from typing import List, Tuple


class Mapping:
    def __init__(self, source_name, dest_name, range_list):
        self.source = source_name
        self.dest = dest_name
        self.map = self.convertToMap(range_list)

    def convertToMap(self, range_list):
        map = []
        for x in range_list:
            dest, source, range = x.split()
            map.append((int(source), int(range), int(dest)))
        return map

    # Maps a single number to a number
    def translate(self, value):
        for x in self.map:
            source, range, dest = x
            if source <= value <= source + range:
                output = dest + (value - source)
                return output
        return value

    # Maps a list of numbers of the form (start, range) to another list of numbers of the form (start, range)
    def translateEnhanced(self, list_of_intervals: List[Tuple[int, int]]):
        mapped_ranges = []
        for interval in list_of_intervals:
            found_match = False
            for x in self.map:
                source, range, dest = x
                if source <= interval[0] <= source + range - 1:
                    # The source is in the range
                    found_match = True
                    if interval[0] + interval[1] <= source + range:
                        # If entirely in range, map the whole interval as it is
                        mapped_ranges.append((dest + (interval[0] - source), interval[1]))
                    else:
                        # Else split it
                        delta = source + range - interval[0]
                        mapped_ranges.append((dest + (interval[0] - source), delta))
                        left_over = (interval[0] + delta, interval[1] - delta)
                        mapped_ranges.extend(self.translateEnhanced([left_over]))
                    break
            if not found_match:
                mapped_ranges.append(interval)
        return mapped_ranges


def part1(file):
    objects = []

    # Parse
    seeds = [int(x.strip()) for x in file[0].split(":")[1].split()]
    for x in file[1:]:
        lines = x.splitlines()
        src, dst = lines[0].split()[0].split("-to-")
        obj = Mapping(src, dst, lines[1:])
        objects.append(obj)

    locations = []
    for seed in seeds:
        step = seed
        for obj in objects:
            step = obj.translate(step)
        locations.append(step)

    print(f'Part 1: {min(locations)}')

def part2(file):
    objects = []

    # Parse
    seeds = [int(x.strip()) for x in file[0].split(":")[1].split()]
    for x in file[1:]:
        lines = x.splitlines()
        src, dst = lines[0].split()[0].split("-to-")
        obj = Mapping(src, dst, lines[1:])
        objects.append(obj)

    locations = []
    for i in range(0, len(seeds), 2):
        step = [(seeds[i], seeds[i+1])]
        for obj in objects:
            step = obj.translateEnhanced(step)
        locations.extend(step)

    output = min(locations, key=lambda x: x[0])[0]
    print(f'Part 2: {output}')


if __name__ == '__main__':
    file = open("input.txt", 'r').read().strip().split("\n\n")

    part1(file)
    part2(file)


