
n, m = map(int, input().split())
CountIn = {i: 0 for i in range(1, n + 1)}
CountOut = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, input().split())
    CountIn[y] += 1
    CountOut[x] += 1

for i in range(1, n + 1):
    print(CountIn[i])
    print(CountOut[i])
