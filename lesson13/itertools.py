
from itertools import combinations, permutations, product


# print(list(product([1, 2, 3], [1, 2, 3], [1, 2, 3])))
# print(list(permutations([1, 2, 3])))
# print(list(combinations([1, 2, 3, 4, 5, 6, 7, 8], 4)))
n, k = map(int, input().split())
# if n < k:
#     print(0)
#     exit(0)

print(len(list(combinations(list(range(n)), k))))
# print(list(c))
