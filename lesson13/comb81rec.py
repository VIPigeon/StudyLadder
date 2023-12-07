
def increase(s):
    res = s[:]
    res[-1] += 1
    i = -1
    while res[i] == 2:
        res[i] = 0
        i -= 1
        res[i] += 1
    return res


def f(s):
    if not all(s):
        f(increase(s))
    print(*s, sep='')


n = int(input())
s = [0] * n
f(s)
# print(*s, sep='')
# for i in range(2**n - 1):
#     increase(s)
#     print(*s, sep='')
