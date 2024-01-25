
n = int(input())
m = []
for i in range(n):
    row = [int(s) for s in input().split()]
    m.append(row)

# print(m)

k = 0
for i in range(n):
    for j in range(n):
        k += m[i][j]

print(k)
