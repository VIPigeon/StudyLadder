
n = int(input())
xs = list(map(int, input().split()))

xs.sort()
ys = []
indX, indY = 0, 0
k = 0

def select():
    global indX, indY
    if indX < len(xs) and indY < len(ys):
        if xs[indX] <= ys[indY]:
            x = xs[indX]
            indX += 1
            return x
        x = ys[indY]
        indY += 1
        return x
    elif indX < len(xs):
        x = xs[indX]
        indX += 1
        return x
    else:
        x = ys[indY]
        indY += 1
        return x

while n > 1:
    x, y = select(), select()
    z = x + y
    k += z
    n -= 1
    ys.append(z)

print(k)
