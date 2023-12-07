"""
8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8
n! = 1 * 2 * ... * (n - 1) * n
1! = 1
0! := 1
"""

from math import factorial
from itertools import combinations


# def C(n, k):
#     return factorial(n) // factorial(k) // factorial(n - k)

res = 1
n, k = map(int, input().split())
if k > n:
    print(0)
    exit(0)
for i in range(n, n - k, -1):
    res *= i
# res *= C(n, k)
res *= len(list(combinations(list(range(n)), k)))
print(res)
