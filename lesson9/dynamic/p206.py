
n, m = map(int, input().split())
a = [[1] * m for i in range(n)]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = a[i - 1][j] + a[i][j - 1]
print(a[-1][-1])
