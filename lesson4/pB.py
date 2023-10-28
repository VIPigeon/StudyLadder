
import math


def dist(x1, y1, x2, y2):
    return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)


def solution():
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())

    oneLight = min(
        max(dist(ax, ay, px, py), dist(ax, ay, 0, 0)),
        max(dist(bx, by, px, py), dist(bx, by, 0, 0))
        )
    r = dist(ax, ay, bx, by) / 4

    if oneLight <= r:
        print(math.sqrt(oneLight))
        return
    if (dist(ax, ay, 0, 0) <= r or dist(bx, by, 0, 0) <= r) and  \
            (dist(ax, ay, px, py) <= r or dist(bx, by, px, py) <= r):
        print(math.sqrt(r))
        return
    if (dist(ax, ay, 0, 0) > r and dist(bx, by, 0, 0) > r) and  \
            (dist(ax, ay, px, py) <= r or dist(bx, by, px, py) <= r):
        print(math.sqrt(min(dist(ax, ay, 0, 0), dist(bx, by, 0, 0))))
        return
    if (dist(ax, ay, px, py) > r and dist(bx, by, px, py) > r) and  \
            (dist(ax, ay, 0, 0) <= r or dist(bx, by, 0, 0) <= r):
        print(math.sqrt(min(dist(ax, ay, px, py), dist(bx, by, px, py))))
        return
    print(
        math.sqrt(max(min(dist(ax, ay, px, py), dist(bx, by, px, py)), min(dist(ax, ay, 0, 0), dist(bx, by, 0, 0)))))


# t = int(input())
# for i in range(t):
#     solution()

for _ in range(int(input())):
    solution()
