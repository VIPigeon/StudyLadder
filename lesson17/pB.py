
# https://codeforces.com/problemset/problem/1886/B


import math


def dist(x1, y1, x2, y2):
    return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)


def bin_search_float(f, l, r):
    if r - l <= 1e-6:
        return l
    m = l + (r - l) / 2
    if f(m):
        r = m
    else:
        l = m
    return bin_search_float(f, l, r)


def check(w):
    w *= w
    if dist(ax, ay, 0, 0) <= w and dist(ax, ay, px, py) <= w:
        return True
    if dist(bx, by, 0, 0) <= w and dist(bx, by, px, py) <= w:
        return True
    if dist(ax, ay, bx, by) > 4 * w:
        return False
    return (dist(ax, ay, 0, 0) <= w or dist(bx, by, 0, 0) <= w)  \
        and (dist(ax, ay, px, py) <= w or dist(bx, by, px, py) <= w)


def solution():
    global px, py, ax, ay, bx, by
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    print(bin_search_float(check, 0, 10000))


px, py, ax, ay, bx, by = 0, 0, 0, 0, 0, 0
for _ in range(int(input())):
    solution()
