
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
prefixes = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefixes[i][j] = prefixes[i - 1][j] + prefixes[i][j - 1]  \
                - prefixes[i - 1][j - 1] + a[i - 1][j - 1]
# print(*prefixes, sep='\n')

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefixes[x2][y2] - prefixes[x1 - 1][y2]  \
            - prefixes[x2][y1 - 1] + prefixes[x1 - 1][y1 - 1])
