
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            # a -= b
            a %= b
        elif b > a:
            # b -= a
            b %= a
    return a + b


a, b = map(int, input().split())
print(gcd(a, b))
