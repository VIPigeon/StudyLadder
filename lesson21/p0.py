
from collections import defaultdict


n = int(input())
graph = defaultdict(set)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for key, value in graph.items():
    print(key, value)

