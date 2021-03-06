def wins(board, calls):
    for i in range(5):
        if all(board[i][j] in calls for j in range(5)):
            return True
        if all(board[j][i] in calls for j in range(5)):
            return True
    return False

def solve(inp):
    sequence, *boards = inp.split("\n\n")

    sequence = [int(x) for x in sequence.split(",")]
    boards = [
        [[int(el) for el in ln.split()] for ln in board.strip().split("\n")]
            for board in boards
    ]

    win_board = None
    win_calls = None

    for i in range(1, len(sequence)):
        calls = set(sequence[:i])

        for board in boards:
            if wins(board, calls):
                win_board = board
                win_calls = sequence[:i]
                break
        else:
            continue
        break

    unmarked = 0
    for i in range(5):
        for j in range(5):
            if win_board[i][j] not in win_calls:
                unmarked += win_board[i][j]

    print(unmarked * win_calls[-1])

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip()
    solve(file)