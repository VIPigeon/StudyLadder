
# https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B

def build(v, l, r):
    global rsq
    if r - l == 1:
        rsq[v] = a[l]
        return
    m = l + (r - l) // 2
    build(v*2 + 1, l, m)
    build(v*2 + 2, m, r)
    rsq[v] = rsq[v*2 + 1] + rsq[v*2 + 2]


def set0(v, l, r, i):
    global rsq
    if r - l == 1:
        rsq[v] = (rsq[v] + 1) % 2
        return
    m = l + (r - l) // 2
    if i < m:
        set0(v*2 + 1, l, m, i)
    else:
        set0(v*2 + 2, m, r, i)
    rsq[v] = rsq[v*2 + 1] + rsq[v*2 + 2]
 
 
def get(v, l, r, k):
    if k > rsq[v]:
        return -1
    if k < 0:
        return -1
    if r - l == 1:
        return l
    m = l + (r - l) // 2

    return max(get(v*2 + 1, l, m, k),  \
            get(v*2 + 2, m, r, k - rsq[v * 2 + 1]))
 
 
n, m = map(int, input().split())
a = list(map(int, input().split()))
rsq = [0] * (n * 4)
 
build(0, 0, n)
 
for _ in range(m):
    q, i = map(int, input().split())
    if q == 1:
        set0(0, 0, n, i)
    else:
        print(get(0, 0, n, i))

