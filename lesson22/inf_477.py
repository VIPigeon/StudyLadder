
n, m = map(int, input().split())
edges = set()
for _ in range(m):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    edges.add((x, y))

if len(edges) == n * (n - 1) // 2:
    print("YES")
else:
    print("NO")
