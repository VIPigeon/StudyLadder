
def getTurns(x1, y1, x2, y2):
    res1 = [
        (x1 + 1, y1 + 2),
        (x1 + 1, y1 - 2),
        (x1 + 2, y1 + 1),
        (x1 + 2, y1 - 1),
        (x1 - 1, y1 + 2),
        (x1 - 1, y1 - 2),
        (x1 - 2, y1 + 1),
        (x1 - 2, y1 - 1)
    ]

    res2 = [
        (x2 + 1, y2 + 2),
        (x2 + 1, y2 - 2),
        (x2 + 2, y2 + 1),
        (x2 + 2, y2 - 1),
        (x2 - 1, y2 + 2),
        (x2 - 1, y2 - 2),
        (x2 - 2, y2 + 1),
        (x2 - 2, y2 - 1)
    ]
    
    for k1 in res1:
        if k1[0] < 0 or k1[0] > 7:
            continue
        if k1[1] < 0 or k1[1] > 7:
            continue
        for k2 in res2:
            if k2[0] < 0 or k2[0] > 7:
                continue
            if k2[1] < 0 or k2[1] > 7:
                continue
            yield (*k1, *k2)
    # for tx1 in (x1 + 2, x1 - 2, x1 + 1, x1 - 1):
    #     if tx1 < 0 or tx1 >= 8:
    #         continue
    #     for ty1 in (y1 + 2, y1 - 2, y1 + 1, y1 - 1):
    #         if ty1 < 0 or ty1 >= 8:
    #             continue
    #         for tx2 in (x2 + 2, x2 - 2, x2 + 1, x2 - 1):
    #             if tx2 < 0 or tx2 >= 8:
    #                 continue
    #             for ty2 in (y2 + 2, y2 - 2, y2 + 1, y2 - 1):
    #                 if ty2 < 0 or ty2 >= 8:
    #                     continue
    #                 yield tx1, ty1, tx2, ty2


D = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}


def transToNumbers(s):
    return D[s[0]], int(s[1]) - 1


def they_on_one_color(x1, y1, x2, y2):
    return (x1 + y1) % 2 == (x2 + y2) % 2


s1, s2 = input().split()
sx1, sy1 = transToNumbers(s1)
sx2, sy2 = transToNumbers(s2)

if not they_on_one_color(sx1, sy1, sx2, sy2):
    print(-1)
    exit(0)
if sx1 == sx2 and sy1 == sy2:
    print(0)
    exit(0)

colors = [[[[False] * 8 for i1 in range(8)] for i2 in range(8)] for i3 in range(8)]
colors[sy1][sx1][sy2][sx2] = True  # значит, что первый конь находится на sx1, sy1, а второй -- на sx2, sy2

"""
cash = {(sx1, sy1, sx2, sy2)} -- тоже можно
"""

queue = [(sx1, sy1, sx2, sy2, 0)]
while queue:
    x1, y1, x2, y2, cnt = queue.pop(0)
    # print(x1, y1, x2, y2, cnt)
    for tx1, ty1, tx2, ty2 in getTurns(x1, y1, x2, y2):
        if colors[ty1][tx1][ty2][tx2]:
            continue
        if tx1 == tx2 and ty1 == ty2:
            # print(tx1, ty1, tx2, ty2)
            print(cnt + 1)
            exit(0)
        queue.append((tx1, ty1, tx2, ty2, cnt + 1))
        colors[ty1][tx1][ty2][tx2] = True
print(-1)
