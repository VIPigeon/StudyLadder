
a = list(map(int, input().split()))
for i in range(len(a) - 2, -1, -1):
    a[i + 1], a[i] = a[i], a[i + 1]
print(*a)

