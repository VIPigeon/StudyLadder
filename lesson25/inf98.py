
n = int(input())
graph = []
for _ in range(n):
    graph.append(set())
    row = input().split()
    for i in range(n):
        if row[i] == '1':
            graph[-1].add(i)


colors = [False] * n
stack = []
for i in range(n):
    if colors[i]:
        continue
    colors[i] = True
    stack.append(i)
    while stack:
        v = stack.pop(-1)
        for u in graph[v]:
            if colors[u]:
                print(1)
                exit(0)
            colors[u] = True
            stack.append(u)
print(0)
