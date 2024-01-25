"""
    0 1 2 3 4

0   0 1 0 0 0
1   1 0 1 1 0
2   0 1 0 1 0
3   0 1 1 0 0
4   0 0 0 0 0


5 4
0 1 2
1 2 2
2 3 4
1 3 1
"""


# https://informatics.msk.ru/mod/statements/view.php?id=359#1


n = int(input())

matrix = []
for i in range(n):
    s = list(map(int, input().split()))
    if s[i] == 1:
        # есть петли
        print("NO")
        exit(0)
    matrix.append(s)
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            print("NO")
            exit(0)
print("YES")
