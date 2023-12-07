
def decrease(s):
    s[-1] -= 1
    i = -1
    while s[i] == -1:
        s[i] = 1
        i -= 1
        s[i] -= 1


n = int(input())
s = [1] * n
print(*s, sep='')
for i in range(2**n - 1):
    decrease(s)
    print(*s, sep='')
