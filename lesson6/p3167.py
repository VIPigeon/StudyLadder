
a = list(map(int, input().split()))

mn = a[0]
mni = 0
mx = a[0]
mxi = 0
for i in range(1, len(a)):
    if mn > a[i]:
        mn = a[i]
        mni = i
    if mx < a[i]:
        mx = a[i]
        mxi = i
a[mni], a[mxi] = a[mxi], a[mni]
print(*a)
