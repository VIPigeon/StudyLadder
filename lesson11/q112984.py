

qFront, qBack = [], []
qCenter = []


def step():
    global qFront, qBack, qCenter
    s = input()
    if s == '-':
        print(qFront.pop(0))
        if len(qFront) < len(qBack):
            if qCenter:
                qFront.append(qCenter.pop(0))
            else:
                qCenter.append(qBack.pop(0))
        return
    s, i = s.split()
    if s == '+':
        qBack.append(i)
        # print(qFront, qCenter, qBack)
        if len(qFront) < len(qBack):
            if qCenter:
                qFront.append(qCenter.pop(0))
            else:
                qCenter.append(qBack.pop(0))
        return
    # s == '*'
    if qCenter:
        qCenter.insert((len(qCenter) + 1) // 2, i)
    else:
        qCenter.append(i)


n = int(input())
for _ in range(n):
    step()
