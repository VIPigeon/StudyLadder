
from collections import defaultdict

n = int(input())

gr = defaultdict(list)

for i in range(1, n + 1):
    gr[i] = [int(s) for s in input().split()]


def print_gr(gr):
    n = len(gr)
    print(n)
    for i in range(1, n + 1):
        print(*gr[i])

# print_gr(gr)

def rev_gr(gr):
    n = len(gr)
    revGr = defaultdict(list)
    for i in range(1, n + 1):
        if i not in revGr:
            revGr[i] = []
        for j in gr[i]:
            revGr[j].append(i)
    return revGr

revGr = rev_gr(gr)
print_gr(revGr)

