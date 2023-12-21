
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A


def build(v, l, r):
    global rmsq
    if r - l == 1:
        rmsq[v][0] = max(a[l], 0)
        rmsq[v][1] = max(a[l], 0)
        rmsq[v][2] = max(a[l], 0)
        rmsq[v][3] = a[l]
        return
    m = l + (r - l) // 2
    build(v*2 + 1, l, m)
    build(v*2 + 2, m, r)
    rmsq[v][0] = max(rmsq[v*2 + 1][0], rmsq[v*2 + 2][0], rmsq[v*2 + 1][2] + rmsq[v*2 + 2][1])
    rmsq[v][1] = max(rmsq[v*2 + 1][1], rmsq[v*2 + 1][3] + rmsq[v*2 + 2][1])
    rmsq[v][2] = max(rmsq[v*2 + 2][2], rmsq[v*2 + 2][3] + rmsq[v*2 + 1][2])
    rmsq[v][3] = rmsq[v*2 + 2][3] + rmsq[v*2 + 1][3]

 
def set0(v, l, r, i, value):
    global rmsq
    if r - l == 1:
        rmsq[v][0] = max(0, value)
        rmsq[v][1] = max(0, value)
        rmsq[v][2] = max(0, value)
        rmsq[v][3] = value
        return
    m = l + (r - l) // 2
    if i < m:
        set0(v*2 + 1, l, m, i, value)
    else:
        set0(v*2 + 2, m, r, i, value)
    rmsq[v][0] = max(rmsq[v*2 + 1][0], rmsq[v*2 + 2][0], rmsq[v*2 + 1][2] + rmsq[v*2 + 2][1])
    rmsq[v][1] = max(rmsq[v*2 + 1][1], rmsq[v*2 + 1][3] + rmsq[v*2 + 2][1])
    rmsq[v][2] = max(rmsq[v*2 + 2][2], rmsq[v*2 + 2][3] + rmsq[v*2 + 1][2])
    rmsq[v][3] = rmsq[v*2 + 2][3] + rmsq[v*2 + 1][3]
 
 
n, m = map(int, input().split())
a = list(map(int, input().split()))
rmsq = [[0, 0, 0, 0] for _ in range(n * 4)]
"""
rmsq[i][0] -- подотрезок с максимальной суммой i-го подотрезка
rmsq[i][1] -- префикс с максимальной суммой i-го подотрезка
rmsq[i][2] -- суффикс с с максимальной суммой i-го подотрезка
rmsq[i][3] -- сумма на i-том подотрезке
"""
 
build(0, 0, n)
print(rmsq[0][0])
 
for _ in range(m):
    a, b = map(int, input().split())
    set0(0, 0, n, a, b)
    print(rmsq[0][0])
