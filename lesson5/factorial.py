"""
6! = 1 * 2 * 3 * 4 * 5 * 6 = 5! * 6
1! = 1

0! := 1
n! = (n - 1)! * n, где n > 0
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(int(input())))
