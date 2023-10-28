
def xor(a, b):
    if (a and b) or (not a and not b):
        return False
    return True


# a, b = map(bool, map(int, input().split()))
a, b = map(int, input().split())
print(int(xor(a, b)))
