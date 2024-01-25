
m, n = int(input())
matrix = [[0] * m for _ in range(m)]
# for i in range(n)
#     row = list(map(int, input().split()))
#     matrix.append(row)
for _ in range(n):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1


"""
matrix[i][j] == 1 -- вершина i связана с вершиной j
matrix[i][j] == 0 -- вершина i не связана с вершиной j
"""
