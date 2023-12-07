

def f(n, k, s):
    if n == k:
        print(s + '1' * k)
        return
    elif k == 0:
        print(s + '0' * n)
        return
    f(n - 1, k, s + '0')
    f(n - 1, k - 1, s + '1')


n, k = map(int, input().split())
f(n, k, '')
