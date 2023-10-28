
def phi(n):
    if (n <= 1):
        return 1
    prev2 = 1  # i - 2
    prev1 = 1  # i - 1
    for i in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


print(phi(int(input())))
