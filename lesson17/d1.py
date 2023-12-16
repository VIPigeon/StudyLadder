
def bin_search_intL(a, l, r, x):
    """
    a[l] <= x < a[r]
    l < r
    """
    if l + 1 == r:
        return l
    m = l + (r - l) // 2
    if x < a[m]:
        r = m
    else:
        l = m
    return bin_search_intL(a, l, r, x)


def bin_searchL(a, x):
    if a[0] > x:
        return 0
    if a[-1] <= x:
        return len(a)
    return bin_search_intL(a, 0, len(a), x) + 1


def bin_search_intR(a, l, r, x):
    """
    a[l] < x <= a[r]
    l < r
    """
    if l + 1 == r:
        return l
    m = l + (r - l) // 2
    if x > a[m]:
        l = m
    else:
        r = m
    return bin_search_intR(a, l, r, x)


def bin_searchR(a, x):
    if a[0] >= x:
        return 0
    if a[-1] < x:
        return len(a)
    return bin_search_intR(a, 0, len(a), x) + 1


n = int(input())
a = sorted(list(map(int, input().split())))
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    i1 = bin_searchR(a, l)
    i2 = bin_searchR(a, r + 1)
    print(i2 - i1)
