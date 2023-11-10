
n = int(input())
a = sorted(list(map(int, input().split())))

res = a[1] - a[0]
b = [0] * n  # b[i] -- количество ниток на i-том гвозде
b[0] = 1
b[1] = 1
for i in range(2, n):
    res += a[i] - a[i - 1]
    if b[i - 2] == 1:
        b[i - 1] = 2
        b[i] = 1
        continue
    b[i - 2] = 1
    b[i] = 1
    res -= a[i - 1] - a[i - 2]
    print(res)
print(res)

