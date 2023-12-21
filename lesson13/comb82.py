
def increase(s):
    s[-1] += 1
    i = -1
    while s[i] == k:
        s[i] = 0
        i -= 1
        s[i] += 1


n, k = map(int, input().split())
s = [0] * n
print(*s, sep='')
for i in range(k**n - 1):
    increase(s)
    print(*s, sep='')

