
from collections import defaultdict


n, m = map(int, input().split())
graph = defaultdict(set)
# graph = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

# for key in sorted(graph.keys()):
for key in range(1, n + 1):
    print(len(graph[key]))

# for v in graph:
#     print(len(v))

