
n, m = map(int, input().split())
res = [[0] * m for _ in range(n)]
# res = [[0] * m] * n  # ошибка!
for i in range(n * m):
    x = i % m
    y = i // m
    res[y][x] = x * y

for row in res:
    print(*row)
    # print(*row, sep='\t')
