
n, s = map(int, input().split())
s -= 1
graph = []
for _ in range(n):
    graph.append(set())
    row = input().split()
    for i in range(n):
        if row[i] == '1':
            graph[-1].add(i)

colors = [False] * n
colors[s] = True
stack = [s]
count = 0
while stack:
    v = stack.pop(-1)
    count += 1
    for u in graph[v]:
        if colors[u]:
            continue
        colors[u] = True
        stack.append(u)
print(count)
