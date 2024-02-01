
n = int(input())
graph = []
for _ in range(n):
    graph.append(set())
    row = input().split()
    for i in range(n):
        if row[i] == '1':
            graph[-1].add(i)

start, finish = map(int, input().split())
if start == finish:
    print(0)
    exit(0)

start -= 1
finish -= 1
colors = [False] * n
colors[start] = True
queue = [(start, [start + 1])]
while queue:
    v, path = queue.pop(0)
    for u in graph[v]:
        if colors[u]:
            continue
        if u == finish:
            print(len(path))
            print(*path, finish + 1)
            exit(0)
        queue.append((u, path + [u + 1]))
        colors[u] = True
print(-1)
