
n = int(input())
m = int(input())
k = int(input())

kn = k // n
km = k // m  # сколько полосок из m кусочек в k

if (k % n == 0 and kn <= m) or  \
        (k % m == 0 and km <= n):
    print("YES")
else:
    print("NO")
