
# from collections import deque
import queue


n = int(input())
kingdoms = list(map(int, input().split()))
kingdoms.sort()

mn = kingdoms[0];
mx = kingdoms[1];
res = 0;
for i in range(2, n):
    if kingdoms[i] < mx:
        buf = mn + kingdoms[i]
        if buf > mx:
            mn = mx
            mx = buf
        else:
            mn = buf
    else:
        buf = mn + mx
        if buf > kingdoms[i]:
            mx = buf
            mn = kingdoms[i]
        else:
            mx = kingdoms[i]
            mn = buf
    res += buf

res += mn + mx
print(res)
