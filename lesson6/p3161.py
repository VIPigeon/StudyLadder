
row = list(map(int, input().split()))
row.append(-1)
aim = int(input())

for i in range(len(row)):
    if row[i] < aim:
        print(i + 1)
        break
