
def my_min(a, b, c, d):
    if a <= b and a <= c and a <= d:
        return a
    if b <= a and b <= c and b <= d:
        return b
    if c <= a and c <= b and c <= d:
        return c
    return d

# print(my_min(1, 2, 3, 4))
print(min(1, 5, 4, 3))
print(max(1, 5, 4, 3))
