
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
flag = False
for y in range(n):
    for x in range(y + 1, n):
        if matrix[y][x] != matrix[x][y]:
            flag = True
            break
    if flag:
        break
if flag:
    print('no')
else:
    print('yes')
