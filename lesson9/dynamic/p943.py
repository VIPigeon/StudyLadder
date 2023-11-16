
n = int(input())
if n >= 1:
    print(1)
if n >= 2:
    pascal = [1, 1]
    print(1, 1)
for _ in range(2, n):
    newPascal = [1]
    # for i in range(len(pascal) - 1):
    #     newPascal.append(pascal[i] + pascal[i + 1])
    for n1, n2 in zip(pascal, pascal[1:]):
        newPascal.append(n1 + n2)
    newPascal.append(1)
    pascal = newPascal[:]
    print(*pascal)
