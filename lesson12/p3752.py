
set0 = set()
n = 0
for e in map(int, input().split()):
    set0.add(e)
    if len(set0) > n:
        n += 1
        print('NO')
    else:
        print('YES')
