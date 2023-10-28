
def gcd(a, b):
    if b == 0:
        return a
    # a > b
    return gcd(b, a % b)


a, b = map(int, input().split())
if a > b:
    print(gcd(a, b))
else:
    print(gcd(b, a))
