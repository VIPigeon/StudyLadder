
from collections import deque


dFront, dBack = deque(), deque()


def step():
    global dFront, dBack
    s = input()
    if s == '-':
        print(dFront.popleft())
        if len(dFront) < len(dBack):
            dFront.append(dBack.popleft())
        return
    s, i = s.split()
    if s == '+':
        dBack.append(i)
        if len(dFront) < len(dBack):
            dFront.append(dBack.popleft())
        return
    # s == '*'
    if len(dFront) > len(dBack):
        dBack.appendleft(i)
    else:
        dFront.append(i)


n = int(input())
for _ in range(n):
    step()
