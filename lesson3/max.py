
# a = int(input())
# b = int(input())
a, b = map(int, input().split())

"""
'2 1'  # input()
['2', '1']  # input().split()
2, 1  # map(int, input().split())
a = 2
b = 1
"""

if a > b:
    print(a)
else:
    print(b)
