
def bin_search_int(a, l, r, x):
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
    return bin_search_int(a, l, r, x)


def bin_search(a, x):
    if a[0] >= x:
        return 0
    if a[-1] < x:
        return len(a)
    return bin_search_int(a, 0, len(a), x) + 1


n, k = map(int, input().split())
a = list(map(int, input().split()))
requests = list(map(int, input().split()))
for r in requests:
    print(bin_search(a, r) + 1)
