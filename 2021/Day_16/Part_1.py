
packets = []

class packet:
    def __init__(self, version, type_id, number, subpackets):
        self.version = version
        self.type_id = type_id
        self.number = number
        self.subpackets = subpackets

    def sum_versions(self):
        if self.subpackets is None:
            return self.version
        return self.version + sum([x.sum_versions() for x in self.subpackets])



def decode_packets(message, curr):
    version = int(message[curr:curr+3], 2)
    type_id = int(message[curr+3:curr+6], 2)
    curr += 6

    if type_id == 4:
        number = ''
        while True:
            group = message[curr:curr+5]
            number += group[1:]
            curr += 5
            if group[0] == '0':
                break
        number = int(number, 2)
        p = packet(version, type_id, number, None)


    else:
        subpackets = []
        length_type = message[curr]
        curr += 1
        if length_type == '0':
            subpacket_length = int(message[curr : curr+15], 2)
            curr += 15
            t = 0
            while t < subpacket_length:
                r, a = decode_packets(message[curr : curr + subpacket_length], t)
                t = a
                subpackets.append(r)
                if all(x == '0' for x in message[curr + t: curr + subpacket_length]):
                    break
            curr += subpacket_length
        if length_type == '1':
            subpacket_number = int(message[curr : curr + 11], 2)
            curr += 11
            n = 0
            t = 0
            while n < subpacket_number:
                r, a = decode_packets(message[curr:], t)
                t = a
                subpackets.append(r)
                n += 1
            curr += t
        p = packet(version, type_id, None, subpackets)
    return p, curr



if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip()

    message = ''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), file)))

    curr = 0

    while curr < len(message):
        p, a = decode_packets(message, curr)
        packets.append(p)
        curr = a
        if all(x == '0' for x in message[curr:]):
            break

    print(f'Part 1: {sum(x.sum_versions() for x in packets)}')
