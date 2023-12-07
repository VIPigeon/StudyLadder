
def setQueen(x, y):
    global gmap
    for i in range(x + 1, n):
        gmap[y][i] += 1
    dx, dy = 1, 1
    while dx + x < n and dy + y < n:
        gmap[y + dy][x + dx] += 1
        dx += 1
        dy += 1
    dx, dy = 1, -1
    while dx + x < n and dy + y >= 0:
        gmap[y + dy][x + dx] += 1
        dx += 1
        dy -= 1


def removeQueen(x, y):
    global gmap
    for i in range(x + 1, n):
        gmap[y][i] -= 1
    dx, dy = 1, 1
    while dx + x < n and dy + y < n:
        gmap[y + dy][x + dx] -= 1
        dx += 1
        dy += 1
    dx, dy = 1, -1
    while dx + x < n and dy + y >= 0:
        gmap[y + dy][x + dx] -= 1
        dx += 1
        dy -= 1


def f(x):
    global answer
    if x == n:
        answer += 1
        return
    for y in range(n):
        if gmap[y][x] == 0:
            setQueen(x, y)
            f(x + 1)
            removeQueen(x, y)


n = int(input())
gmap = [[0] * n for _ in range(n)]
answer = 0
f(0)
print(answer)
