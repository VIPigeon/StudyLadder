
def f(n, res):
    if n == 0:
        print(*res, sep='')
        return
    global gmap
    for i in range(N):
        if not gmap[i]:
            gmap[i] = True
            f(n - 1, res + [i + 1])
            gmap[i] = False


N = int(input())
gmap = [False] * N
f(N, [])
