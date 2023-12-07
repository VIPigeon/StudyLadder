
n = int(input())
a = list(map(int, input().split()))

prefixes = [0]
for e in a:
    prefixes.append(e + prefixes[-1])
# print(prefixes)

k = int(input())
for _ in range(k):
    left, right = map(int, input().split())
    print(prefixes[right] - prefixes[left - 1], end=' ')
