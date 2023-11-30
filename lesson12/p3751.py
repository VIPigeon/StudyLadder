
# from collections import Counter

print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))
# a = Counter(map(int, input().split()))
# b = Counter(map(int, input().split()))
# res = []
# for key in a.keys() & b.keys():
#     for _ in range(min(a[key], b[key])):
#         res.append(key)
#     # print(*([key] * min(a[key], b[key])), end=' ')
# print(*sorted(res))
