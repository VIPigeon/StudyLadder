
def build(v, l, r):
    global tree
    if r - l == 1:
        tree[v][0] = a[l]
        tree[v][1] = 1
        return
    m = l + (r - l) // 2
    build(v*2 + 1, l, m)
    build(v*2 + 2, m, r)

    v1 = tree[v*2 + 1]
    v2 = tree[v*2 + 2]
    if v1[0] < v2[0]:
        tree[v] = v1[:]
    elif v1[0] > v2[0]:
        tree[v] = v2[:]
    else:
        tree[v][0] = v1[0]
        tree[v][1] = v1[1] + v2[1]


def set0(v, l, r, i, value):
    global tree
    if r - l == 1:
        tree[v] = [value, 1]
        return
    m = l + (r - l) // 2
    if i < m:
        set0(v*2 + 1, l, m, i, value)
    else:
        set0(v*2 + 2, m, r, i, value)

    v1 = tree[v*2 + 1]
    v2 = tree[v*2 + 2]
    if v1[0] < v2[0]:
        tree[v] = v1[:]
    elif v1[0] > v2[0]:
        tree[v] = v2[:]
    else:
        tree[v][0] = v1[0]
        tree[v][1] = v1[1] + v2[1]


def get(v, l, r, xl, xr):
    if xr <= l or r <= xl:
        return [1e10, 0]
    if xl <= l and r <= xr:
        return tree[v]
    m = l + (r - l) // 2

    v1 = get(v*2 + 1, l, m, xl, xr)
    v2 = get(v*2 + 2, m, r, xl, xr)
    if v1[0] < v2[0]:
        return v1
    if v1[0] > v2[0]:
        return v2
    return [v1[0], v1[1] + v2[1]]


n, m = map(int, input().split())
a = list(map(int, input().split()))
tree = [[0, 0] for _ in range(n * 4)]
"""
tree[i][0] -- минимум на i-том отрезке
tree[i][1] -- количество минимальных элементов на i-том отрезке
"""

build(0, 0, n)

for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 1:
        set0(0, 0, n, a, b)
    else:
        print(*get(0, 0, n, a, b))
