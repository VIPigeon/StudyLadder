
def getS(d, h, y):
    # y -- координата среза относительно верхней точки
    # d, h -- параметры исходного треугольника
    p = y / h
    return y * p * d / 2


def solution():
    n, d, h = map(int, input().split())
    coords = list(map(int, input().split()))
    res = d * h / 2
    for i in range(1, n):
        y = coords[i]
        prev = coords[i - 1]
        res += d * h / 2
        if prev + h > y:
            res -= getS(d, h, prev + h - y)
    print(res)


for _ in range(int(input())):
    solution()
