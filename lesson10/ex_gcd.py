
def ex_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = ex_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1


a, b = map(int, input().split())
print(*ex_gcd(a, b))
