
def increase(a):
    """
    for e in a:  # don't work
        e += 1
    """
    for i in range(len(a)):
        a[i] += 1


"""
int
float
bool

str
list
"""

a = [1, 2, 3, 4, 5]
# b = a  # copy adress

# b1 = a.copy()
# b2 = a[:]

# increase(a)
# print(a)
# print(b)

# n = int(input())
# buf = []
# for _ in range(n):
#     buf.append(a[:])

# buf = [a[:] for _ in range(n)]


# buf[0][0] = 10

# print(*buf, sep='\n')


list4x4 = [[0] * 4 for _ in range(4)]
# list4x4 = []
# for _ in range(4):
#     list4x4.append([0] * 4)

list4x4[0][0] = 1
print(*list4x4, sep='\n')
