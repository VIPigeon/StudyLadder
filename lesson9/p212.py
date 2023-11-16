
def solve(ws):
    ans = [0] * (len(ws) + 1)
    for k in range(len(ws)):
        s = ws[k][0] + ans[k]

        if k > 0:
            s = min(s, ws[k - 1][1] + ans[k - 1])
        
        if k > 1:
            s = min(s, ws[k - 2][2] + ans[k - 2])

        ans[k + 1] = s

    return ans[-1]


n = int(input())
ws = []
for _ in range(n):
    a, b, c = map(int, input().split())
    ws.append((a, b, c))

print(solve(ws))
