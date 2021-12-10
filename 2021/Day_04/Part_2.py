board = []

def check_number(num):
    winners = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            for z in range(len(board[x][y])):
                if board[x][y][z] == num:
                    board[x][y][z] = None
                    if all(t is None for t in board[x][y]) or all(t is None for t in list(zip(*board[x]))[z]):
                        winners.append(board[x])
    return winners

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n\n')

    drawn = [int(x) for x in file[0].split(',')]    # Get the called numbers

    for x in file[1:]:                              # Boards into list of matrixes
        b = []
        for y in x.split('\n'):
            b.append([int(x) for x in y.split()])
        board.append(b)

    for x in drawn:
        winners = check_number(x)
        if winners:
            if len(board) != 1:
                for w in winners:
                    board.remove(w)
            else:
                break
    output = (sum([sum(list(filter(None, x))) for x in board[0]])) * x

    print(f'Part 2: {output}')