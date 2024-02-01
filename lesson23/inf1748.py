
def getTurns(v):
    return v + 3, v * 4



a, b = map(int, input().split())
if a == b:
    print(0)
    exit(0)

colors = [False] * (b + 1)
colors[a] = True
queue = [(a, 0)]
while queue:
    v, cnt = queue.pop(0)
    for u in getTurns(v):
        if u > b or colors[u]:
            continue
        if u == b:
            print(cnt + 1)
            exit(0)
        colors[u] = True
        queue.append((u, cnt + 1))
print(-1)
