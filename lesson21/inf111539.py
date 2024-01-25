
n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1
    # matrix[b - 1][a - 1] = 1

for row in matrix:
    print(*row)

