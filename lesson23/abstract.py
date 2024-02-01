
def getTurns(v):
    return graph[v]  # например


def isLegal(u):
    if colors[u]:
        return False
    ...
    return True


def printAnswer():
    print("Есть путь")


graph = []
queue = []
colors = [...]  # задается списком, словарем или сэтом
while queue:
    v = queue.pop(0)
    for u in getTurns(v):
        if not isLegal(u):
            continue
        if isFinal(u):
            printAnswer()
            exit(0)
        queue.append(v)
        colors[u] = True
print("Нет пути")
