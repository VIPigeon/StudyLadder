
import math


def is_prime(n):
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def erat(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i + i, n + 1, i):
                isPrime[j] = False
    return isPrime[n]


n = int(input())
if erat(n):
    print("prime")
else:
    print("composite")

# if is_prime(n):
#     print("prime")
# else:
#     print("composite")
