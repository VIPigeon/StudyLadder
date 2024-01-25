
n = int(input())
m = []
for i in range(n):
    row = [int(s) for s in input().split()]
    m.append(row)

# print(m)

for i in range(n):
    if m[i][i] != 0:
        print("NO")
        exit(0)

for i in range(n):
    for j in range(i):
        if m[i][j] != m[j][i]:
            print("NO")
            exit(0)

print("YES")
