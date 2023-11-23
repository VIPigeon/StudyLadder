
from collections import deque


deq = deque()


def processing(c):
    global deq
    if c == 'size':
        print(len(deq))
    elif c == 'clear':
        deq = deque()
        print('ok')
    elif c == 'pop_front':
        print(deq.pop())
    elif c == 'pop_back':
        print(deq.popleft())
    elif c == 'front':
        e = deq.pop()
        print(e)
        deq.append(e)
    elif c == 'back':
        e = deq.popleft()
        print(e)
        deq.appendleft(e)
    else:
        c, n = c.split()
        if c == "push_front":
            deq.append(int(n))
        else:
            deq.appendleft(int(n))
        print('ok')


command = input()
while command != 'exit':
    processing(command)
    command = input()
print('bye')
