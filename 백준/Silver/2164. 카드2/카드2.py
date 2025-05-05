from collections import deque

N = int(input())
ar = deque([i for i in range(1, N + 1)])

while N != 1:
    ar.popleft()
    if len(ar) == 1:
        break
    x = ar.popleft()
    ar.append(x)

print(*ar)