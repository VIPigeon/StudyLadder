
a = list(map(int, input().split()))
k = int(input())

n = len(a)
loop = 0
buf = a[0]
i = 0
for j in range(n):
    i = (i + k) % n
    buf, a[i] = a[i], buf
    if i == loop:
        i = (i + 1) % n
        loop += 1
        buf = a[i]
print(*a)
