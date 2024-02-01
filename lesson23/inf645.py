
def getTurns(x, y):
    return [(x + 1, y),  \
            (x - 1, y),  \
            (x, y + 1),  \
            (x, y - 1)]


def printAnswer(path):
    print('Y')
    # print(path)
    for x, y in path:
        board[y][x] = '+'
    for row in board:
        print(*row, sep='')

n = int(input())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(n):
        if board[i][j] == '@':
            sX, sY = j, i
cash = {(sX, sY)}
queue = [(sX, sY, [])]
while queue:
    vX, vY, path = queue.pop(0)
    for tX, tY in getTurns(vX, vY):
        if tX < 0 or tX >= n or tY < 0 or tY >= n:
            continue
        if (tX, tY) in cash:
            continue
        if board[tY][tX] == 'O':
            continue
        if board[tY][tX] == 'X':
            printAnswer(path + [(tX, tY)])
            exit(0)
        queue.append((tX, tY, path + [(tX, tY)]))
        cash.add((tX, tY))
print('N')
