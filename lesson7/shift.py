
def shift(a, k):
    buf = a[0]
    i = 0
    loopStart = 0
    n = len(a)
    
    for _ in range(n):
        i = (i + k) % n
        buf, a[i] = a[i], buf
        if i == loopStart:
            i = (i + 1) % n
            loopStart += 1
            buf = a[i]


a = list(map(int, input().split()))
k = int(input())
shift(a, k)
print(*a)
