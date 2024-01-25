
from collections import defaultdict

n, m = map(int, input().split())
gr = defaultdict(set)
for _ in range(m):
    x, y = map(int, input().split())
    gr[x].add(y)
    gr[y].add(x)

for i in range(1, n + 1):
    for j in gr[i]:
        for k in gr[j]:
            if i != k and k not in gr[i]:
                print("NO")
                exit(0)

print("YES")
