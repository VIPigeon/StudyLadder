
n = int(input())
m = []
for i in range(n):
    row = [int(s) for s in input().split()]
    m.append(row)

for i in range(n):
    for j in range(i):
        if m[i][j] == 1:
            print(j + 1, i + 1)
