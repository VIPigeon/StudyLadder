
def build(v, l, r):
    global tree
    if r - l == 1:
        tree[v] = a[l]
        return
    m = l + (r - l) // 2
    build(v*2 + 1, l, m)
    build(v*2 + 2, m, r)

    tree[v] = tree[v*2 + 1] + tree[v*2 + 2]


def set0(v, l, r, i):
    global tree
    if r - l == 1:
        tree[v] = (tree[v] + 1) % 2
        return
    m = l + (r - l) // 2
    if i < m:
        set0(v*2 + 1, l, m, i)
    else:
        set0(v*2 + 2, m, r, i)

    tree[v] = tree[v*2 + 1] + tree[v*2 + 2]


def get(v, l, r, k):
    if k > tree[v]:
        return -1
    if k < 0:
        return -1
    if r - l == 1:
        return l
    m = l + (r - l) // 2

    get1 = get(v*2 + 1, l, m, k)
    get2 = get(v*2 + 2, m, r, k - tree[v*2 + 1])
    return max(get1, get2)


n, m = map(int, input().split())
a = list(map(int, input().split()))
tree = [0 for _ in range(n * 4)]

build(0, 0, n)

for _ in range(m):
    q, i = map(int, input().split())
    if q == 1:
        set0(0, 0, n, i)
    else:
        print(get(0, 0, n, i))
