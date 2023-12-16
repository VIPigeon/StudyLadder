
def bin_search_int(f, l, r):
    if l + 1 == r:
        return l
    m = l + (r - l) // 2
    if f(m):
        r = m
    else:
        l = m
    return bin_search_int(f, l, r)


def bin_search(f):
    if n == 1:
        return x
    return bin_search_int(f, x, n * y) + 1


def check(t):
    t -= x
    return int((1/x) * t) + int((1/y) * t) + 1 >= n


n, x, y = map(int, input().split())
if y < x:
    x, y = y, x
print(bin_search(check))

