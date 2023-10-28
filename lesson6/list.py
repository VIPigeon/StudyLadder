
a = [1, 2, 3, 4, 5, 6, 7]

a[3] = 18
a[1:4]
a[::-1]

a.append(14)

# -------------------------------
# a.copy()
# a[:]  # идентично

a.pop(3)
a.pop()
a.pop(-1)

a.remove(18)

a.reverse()
for e in reversed(a):
    ...

a.sort()
sorted(a)
a.sort(reversed=True)
sorted(a, reversed=True)

max(a)
min(a)

a.find(18)
a.count(2)
