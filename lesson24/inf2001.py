

def getTurns(n1, n2, n3, n4):
    if n1 != 9:
        yield (n1 + 1, n2, n3, n4)
    if n4 != 1:
        yield (n1, n2, n3, n4 - 1)
    yield (n4, n1, n2, n3)
    yield (n2, n3, n4, n1)


def printAnswer(path):
    for n in path:
        print(*n, sep='')


a = tuple(map(int, list(input())))
b = tuple(map(int, list(input())))
if a == b:
    print(0)
    exit(0)

cash = {a}
queue = [(a, [a])]
while True:
    v, path = queue.pop(0)
    for u in getTurns(*v):
        if u in cash:
            continue
        if u == b:
            printAnswer(path + [b])
            exit(0)
        cash.add(u)
        queue.append((u, path + [u]))
