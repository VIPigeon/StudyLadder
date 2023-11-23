
"""
Даны числа N и M. Собрать матрицу NxM, в которой все ячейки будут пронумерованы слева направо, сверху вниз
То есть для N = 2, M = 3 ответом будет матрица

1 2 3
4 5 6
"""


N, M = map(int, input().split())
matrix = [[i * M + j + 1 for j in range(M)] for i in range(N)]

for row in matrix:
    print(*row, sep='\t')
