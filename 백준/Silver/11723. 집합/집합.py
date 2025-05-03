import sys
input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
S = 0

for _ in range(M):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        S |= (1 << int(cmd[1]))
    elif op == "remove":
        S &= ~(1 << int(cmd[1]))
    elif op == "check":
        result = 1 if S & (1 << int(cmd[1])) else 0
        write(str(result) + '\n')  # 빠른 출력
    elif op == "toggle":
        S ^= (1 << int(cmd[1]))
    elif op == "all":
        S = (1 << 21) - 1
    elif op == "empty":
        S = 0