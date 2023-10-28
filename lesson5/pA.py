
def solution():
    n = int(input())
    """
    n % 3 != 0
        1 + 2 + (n - 3)

    n % 3 == 0
        1 + 4 + (n - 5)

    Исключения:
        n < 7
        n == 9
    """
    if n < 7 or n == 9:
        print("NO")
        return

    print("YES")
    if n % 3 != 0:
        print(1, 2, n - 3)
        return
    print(1, 4, n - 5)


for _ in range(int(input())):
    solution()
