a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = c - a
f = d - b
# if(f >= 100):
#     e = e + (f // 100)
#     f = f % 100
#     print(e, f)
# else:
#     print(e, f)
print(e + f // 100, f % 100)
