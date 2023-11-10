
n = int(input())
a = list(map(int, input().split()))
for i in range(2, n):
    a[i] += min(a[i - 1], a[i - 2])
print(a[-1])
