
from collections import defaultdict


n, m = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

colors = [False] * (n + 1)
stack = []
for i in range(1, n + 1):
    if colors[i]:
        continue
    colors[i] = 1
    stack.append(i)
    while stack:
        v = stack.pop(-1)
        for u in graph[v]:
            if colors[u] == colors[v]:
                print('NO')
                exit(0)
            if colors[u]:
                continue
            # colors[u] = ((colors[v] + 1) % 2) + 1
            if colors[v] == 1:
                colors[u] = 2
            else:
                colors[u] = 1
            stack.append(u)
print('YES')
for i in range(1, n + 1):
    if colors[i] == 1:
        print(i, end=' ')
