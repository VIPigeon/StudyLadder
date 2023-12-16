
def bin_search_intR(f, l, r):
    """
    a[l] < x <= a[r]
    l < r
    """
    if l + 1 == r:
        return l
    m = l + (r - l) // 2
    if f(m):
        r = m
    else:
        l = m
    return bin_search_intR(f, l, r)


def bin_searchR(f):
    if f(0):
        return 0
    return bin_search_intR(f, 0, n * max(w, h)) + 1


def check(x):
    # x -- сторона квадрата
    k1 = x // w
    k2 = x // h
    return k1 * k2 >= n


w, h, n = map(int, input().split())
print(bin_searchR(check))
