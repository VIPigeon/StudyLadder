
def increase(s):
    s[-1] += 1
    i = -1
    while s[i] == 2:
        s[i] = 0
        i -= 1
        s[i] += 1


n = int(input())
s = [0] * n
print(*s, sep='')
for i in range(2**n - 1):
    increase(s)
    print(*s, sep='')
