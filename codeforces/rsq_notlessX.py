
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C
 
 
def f(x, y):
    return max(x,y)
 
 
def build(v, left, right):
    if left + 1 == right:
        tree[v] = a[left]
    else:
        m = (left + right) // 2
        build(v * 2 + 1, left, m)
        build(v * 2 + 2, m, right)
        tree[v] = f(tree[2 * v + 1], tree[2 * v + 2])
 
 
def set0(v, left, right, i, newValue):
    if left + 1 == right:
        tree[v] = newValue
    else:
        m = (left + right) // 2
        if i < m:
            set0(v * 2 + 1, left, m, i, newValue)
        else:
            set0(v * 2 + 2, m, right, i, newValue)
        tree[v] = f(tree[2 * v + 1], tree[2 * v + 2])
 
 
def get(v, left, right, x):
    if right - left == 1:
        return left
    mid = (left + right) // 2
    if tree[2 * v + 1] >= x:
        return get(2 * v + 1, left, mid, x)
    return get(2 * v + 2, mid, right, x)
 
 
n, m = map(int, input().split())
a = list(map(int, input().split()))
MAXN = 100000
tree = [0] * (MAXN * 4)
build(0, 0, n)

for i in range(m):
    request = list(map(int, input().split()))
    if request[0] == 1:
        set0(0, 0, n, request[1], request[2])
    else:
        if request[1] > tree[0]:
            print(-1)
        else:
            print(get(0, 0, n, request[1]))
