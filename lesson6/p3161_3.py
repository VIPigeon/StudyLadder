
row = list(map(int, input().split()))
aim = int(input())

for i in range(len(row)):
    if row[i] < aim:
        print(i + 1)
        break
else:
    print(len(row) + 1)
