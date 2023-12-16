
def build(v, l, r):
    global rsq
    if r - l == 1:
        rsq[v] = a[l]
        return
    m = l + (r - l) // 2
    build(v*2 + 1, l, m)
    build(v*2 + 2, m, r)
    rsq[v] = rsq[v*2 + 1] + rsq[v*2 + 2]


def set0(v, l, r, i, value):
    global rsq
    if r - l == 1:
        rsq[v] = value
        return
    m = l + (r - l) // 2
    if i < m:
        set0(v*2 + 1, l, m, i, value)
    else:
        set0(v*2 + 2, m, r, i, value)
    rsq[v] = rsq[v*2 + 1] + rsq[v*2 + 2]


def get(v, l, r, xl, xr):
    if xr <= l or r <= xl:
        # print(v, 0)
        return 0
    if xl <= l and r <= xr:
        # print(v, rsq[v])
        return rsq[v]
    m = l + (r - l) // 2
    return get(v*2 + 1, l, m, xl, xr) +  \
        get(v*2 + 2, m, r, xl, xr)


n, m = map(int, input().split())
a = list(map(int, input().split()))
rsq = [0] * (n * 4)

build(0, 0, n)

for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 1:
        set0(0, 0, n, a, b)
    else:
        print(get(0, 0, n, a, b))
