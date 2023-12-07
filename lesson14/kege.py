
from itertools import product


# Сколько существует шестеричных семизначных чисел, содержащих в своей записи ровно одну цифру 2, при этом никакая чётная цифра не стоит рядом с цифрой 2?


def check(p):
    if p.count(2) != 1:
        return False
    i = 0
    for j in range(7):
        if p[j] == 2:
            i = j
            break
    if i - 1 >= 0 and p[i - 1] % 2 == 0:
        return False
    if i + 1 < 7 and p[i + 1] % 2 == 0:
        return False
    return True


res = 0
for p in product([1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]):
    if check(p):
        res += 1
print(res)
