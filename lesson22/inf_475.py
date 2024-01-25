
n, m = map(int, input().split())
Count = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, input().split())
    Count[y] += 1
    Count[x] += 1

k = Count[1]
if all(Count[i] == k for i in range(2, n + 1)):
    print("YES")
else:
    print("NO")
