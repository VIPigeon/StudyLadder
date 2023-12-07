
n = int(input())
xs = sorted(list(map(int, input().split())))
ys = [xs[0] + xs[1]]

i = 2
j = 0

res = ys[0]


# def popMin():
#     global res, i, j
#     if len(xs) > i and xs[i] <= ys[j]:
#         i += 1
#         return xs[i - 1]
#     j += 1
#     return ys[j - 1]


def popMin():
    global i, j
    if len(ys) <= j:
        i += 1
        return xs[i - 1]
    if len(xs) <= i:
        j += 1
        return ys[j - 1]
    if xs[i] <= ys[j]:
        i += 1
        return xs[i - 1]
    j += 1
    return ys[j - 1]



for _ in range(n - 2):
    a, b = popMin(), popMin()
    res += a + b
    ys.append(a + b)

print(res)
