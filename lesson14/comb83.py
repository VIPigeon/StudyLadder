
def decrease(s):
    s[-1] -= 1
    i = -1
    while s[i] == -1:
        s[i] = k - 1
        i -= 1
        s[i] -= 1


def printN(s):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    for c in s:
        print(alphabet[c], end='')
    print()


# for i in range(65, 65 + 26):
#     print(chr(i), end='')
n, k = map(int, input().split())
s = [k - 1] * n
# print(*s, sep='')
printN(s)
for i in range(k**n - 1):
    decrease(s)
    printN(s)
    # print(*s, sep='')
