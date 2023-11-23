
stack = []


def processing(c):
    global stack
    if c == 'size':
        print(len(stack))
    elif c == 'clear':
        stack = []
        print('ok')
    elif c == 'back':
        print(stack[-1])
    elif c == 'pop':
        print(stack.pop(-1))
    else:
        c, n = c.split()
        stack.append(int(n))
        print('ok')


command = input()
while command != 'exit':
    processing(command)
    command = input()
print('bye')
