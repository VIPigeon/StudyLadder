
queue = []


def processing(c):
    global queue
    if c == 'size':
        print(len(queue))
    elif c == 'clear':
        queue = []
        print('ok')
    elif c == 'front':
        print(queue[0])
    elif c == 'pop':
        print(queue.pop(0))
    else:
        c, n = c.split()
        queue.append(int(n))
        print('ok')


command = input()
while command != 'exit':
    processing(command)
    command = input()
print('bye')
