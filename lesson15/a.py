
n = int(input())
c1, c2 = 0, 0
for c in list(map(int, input().split())):
    if c == 1:
        c1 += 1
    else:
        c2 += 1

if c2:
    print(2, end=' ')
    c2 -= 1
if c1:
    print(1, end=' ')
    c1 -= 1
while c2:
    print(2, end=' ')
    c2 -= 1
while c1:
    print(1, end=' ')
    c1 -= 1
