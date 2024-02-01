
def getTurns(x, y):
    return (x + 2, y + 1),  \
            (x - 2, y + 1),  \
            (x + 2, y - 1),  \
            (x - 2, y - 1),  \
            (x - 1, y - 2),  \
            (x - 1, y + 2),  \
            (x + 1, y + 2),  \
            (x + 1, y + 2)


def printAnswer(path):
    print(len(path) - 1)
    for x, y in path:
        print(x, y)


n = int(input())
sX, sY = map(int, input().split())
fX, fY = map(int, input().split())

colors = [[False] * (n + 1) for _ in range(n + 1)]
colors[sY][sX] = True
queue = [(sX, sY, [(sX, sY)])]
while queue:
    x, y, path = queue.pop(0)
    for tX, tY in getTurns(x, y):
        if tX <= 0 or tX > n or tY <= 0 or tY > n:
            continue
        if colors[tY][tX]:
            continue
        if tX == fX and tY == fY:
            printAnswer(path + [(tX, tY)])
            exit(0)
        queue.append((tX, tY, path + [(tX, tY)]))
        colors[tY][tX] = True
