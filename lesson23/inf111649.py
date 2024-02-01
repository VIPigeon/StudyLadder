
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
queue = [(start, 0)]
while queue:
    v, distance = queue.pop(0)
    for u in graph[v]:
        if colors[u]:
            continue
        if u == finish:
            print(distance + 1)
            exit(0)
        queue.append((u, distance + 1))
        colors[u] = True
print(-1)
