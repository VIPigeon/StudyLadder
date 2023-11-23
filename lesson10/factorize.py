
import math


def factorize(n):
    res = []
    # for d in range(2, n + 1):
    for d in range(2, int(math.sqrt(n)) + 1):
        while n % d == 0:
            n //= d
            res.append(d)
        if n == 1:
            return res
    res.append(n)
    return res


n = int(input())
print(*factorize(n))
