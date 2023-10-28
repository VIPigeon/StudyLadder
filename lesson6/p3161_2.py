
row = list(map(int, input().split()))
aim = int(input())

flag = True
for i in range(len(row)):
    if row[i] < aim:
        print(i + 1)
        flag = False
        break
if flag:
    print(len(row) + 1)
