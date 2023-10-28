# https://codeforces.com/contest/1886/problem/B?locale=ru

import math


def dist(x1, y1, x2, y2):
    return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)


def solution():
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    oneLight = min(
            max(dist(0, 0, ax, ay), dist(px, py, ax, ay)), 
            max(dist(0, 0, bx, by), dist(px, py, bx, by))
            )
    r = dist(ax, ay, bx, by) / 4

    # все можно осветить только одним фонарем
    if oneLight <= r:
        print(math.sqrt(oneLight))
        return

    # все освещено
    if (dist(0, 0, ax, ay) <= r or dist(0, 0, bx, by) <= r) and  \
            (dist(px, py, ax, ay) <= r or dist(px, py, bx, by) <= r):
        print(math.sqrt(r))
        return

    # только O не освещена
    if (dist(0, 0, ax, ay) > r and dist(0, 0, bx, by) > r) and  \
            (dist(px, py, ax, ay) <= r or dist(px, py, bx, by) <= r):
        print(math.sqrt(min(
                    dist(ax, ay, 0, 0), dist(bx, by, 0, 0)
                    )))
        return

    # только P не освещена
    if (dist(px, py, ax, ay) > r and dist(px, py, bx, by) > r) and  \
            (dist(0, 0, ax, ay) <= r or dist(0, 0, bx, by) <= r):
        print(math.sqrt(min(
                    dist(ax, ay, px, py), dist(bx, by, px, py)
                    )))
        return

    # обе точки не освещены
    print(math.sqrt(max(
            min(dist(px, py, ax, ay), dist(px, py, bx, by)),
            min(dist(0, 0, ax, ay), dist(0, 0, bx, by))
            )))


t = int(input())
for _ in range(t):
    solution()
