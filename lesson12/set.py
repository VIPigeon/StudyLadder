
a = set()
b = {1, 23, 4, 5, "asd"}
print(len(a), len(b))
# b[1] -- wrong!
print(4 in b)
c = {1, 1, 1, 1, 1}
c.add("ff")
c.remove("ff")
print(c)

set1 = {1, 2, 3, 4}
set2 = {2, 3, 6, 7, 8}
print(set1 | set2)
print(set1 & set2)

for e in set2:
    print(e, end=', ')
print()
