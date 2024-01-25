
def build(v, l, r):
    global tree
    if r - l == 1:
        tree[v][0] = max(0, a[l])
        tree[v][1] = max(0, a[l])
        tree[v][2] = max(0, a[l])
        tree[v][3] = a[l]
        return
    m = l + (r - l) // 2
    build(v*2 + 1, l, m)
    build(v*2 + 2, m, r)

    v1 = tree[v*2 + 1]
    v2 = tree[v*2 + 2]
    tree[v][0] = max(v1[0], v2[0], v1[2] + v2[1])
    tree[v][1] = max(v1[1], v1[3] + v2[1])
    tree[v][2] = max(v2[2], v2[3] + v1[2])
    tree[v][3] = v1[3] + v2[3]


def set0(v, l, r, i, value):
    global tree
    if r - l == 1:
        tree[v][0] = max(0, value)
        tree[v][1] = max(0, value)
        tree[v][2] = max(0, value)
        tree[v][3] = value
        return
    m = l + (r - l) // 2
    if i < m:
        set0(v*2 + 1, l, m, i, value)
    else:
        set0(v*2 + 2, m, r, i, value)
    v1 = tree[v*2 + 1]
    v2 = tree[v*2 + 2]
    tree[v][0] = max(v1[0], v2[0], v1[2] + v2[1])
    tree[v][1] = max(v1[1], v1[3] + v2[1])
    tree[v][2] = max(v2[2], v2[3] + v1[2])
    tree[v][3] = v1[3] + v2[3]


n, m = map(int, input().split())
a = list(map(int, input().split()))
tree = [[0, 0, 0, 0] for _ in range(n * 4)]
"""
tree[i][0] -- отрезок с максимальной суммой на i-том отрезке
tree[i][1] -- префикс с максимальной суммой на i-том отрезке
tree[i][2] -- суффикс с максимальной суммой элементов на i-том отрезке
tree[i][3] -- сумма на i-том отрезке
"""

build(0, 0, n)
print(tree[0][0])

for _ in range(m):
    a, b = map(int, input().split())
    set0(0, 0, n, a, b)
    print(tree[0][0])
