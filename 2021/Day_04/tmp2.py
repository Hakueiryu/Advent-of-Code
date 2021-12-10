def p2(f):
    nums = [int(x) for x in f.readline().strip().split(",")]
    boards = [
        [[int(i) for i in l.split()] for l in x.splitlines()]
        for x in f.read().strip().split("\n\n")
    ]

    wins = []
    win = None

    for num in nums:
        if sum(x not in wins for x in boards) == 1:
            win = next(i for i, x in enumerate(boards) if x not in wins)
        for bb, board in enumerate(boards):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == num:
                        board[i][j] = None
            for row in board:
                if all(x is None for x in row):
                    if bb == win:
                        score = sum(i for r in board for i in r if i is not None)
                        return score * num
                    wins.append(board)
            for col in zip(*board):
                if all(x is None for x in col):
                    if bb == win:
                        score = sum(i for r in board for i in r if i is not None)
                        return score * num
                    wins.append(board)

if __name__ == '__main__':
    file = open('input.txt', 'r')
    print(p2(file))