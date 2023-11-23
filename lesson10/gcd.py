"""
gcd(a, b) = gcd(a - b, b), где a > b
...
a == b
gcd(a, a) = a
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
if a > b:
    print(gcd(a, b))
elif a == b:
    print(a)
else:
    print(gcd(b, a))
