
def solution():
    s = input()
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
            continue
        if len(stack) == 0:
            print('no')
            return
        p = stack.pop(-1)
        if c == ')' and p == '(':
            continue
        if c == ']' and p == '[':
            continue
        if c == '}' and p == '{':
            continue
        print('no')
        return
    if len(stack):
        print('no')
    else:
        print('yes')


solution()
