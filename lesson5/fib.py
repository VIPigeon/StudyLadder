
from functools import lru_cache

"""
1 1 2 3 5 8 13...
phi(0) := 1
phi(1) := 1
phi(n) = phi(n - 1) + phi(n - 2), где n >= 2
"""

@lru_cache
def phi(n):
    if n <= 1:
        return 1
    return phi(n - 1) + phi(n - 2)


phi(15)
print(phi(int(input())))
