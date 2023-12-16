
def bin_search_float(f, l, r):
    if r - l <= 1e-6:
        return l
    m = l + (r - l) / 2
    if f(m):
        l = m
    else:
        r = m
    return bin_search_float(f, l, r)


def check(x):
    # x -- длина куска
    res = 0
    for e in a:
        res += e // x
        if res >= k:
            return True
    return False


n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(float(input()))
print(bin_search_float(check, 0, max(a) + 1e-6))
