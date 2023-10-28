
def solution():
    a, b, c = map(int, input().split())
    if b > a:
        a, b = b, a
    # a > b
    res = 0
    while a > b:
        a -= c
        b += c
        res += 1
    print(res)


for _ in range(int(input())):
    solution()
