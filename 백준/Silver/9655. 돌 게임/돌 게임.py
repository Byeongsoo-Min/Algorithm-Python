N = int(input())
dp = [-1] * (1001)
dp[1] = 0 #상근
dp[2] = 1 #창영
dp[3] = 0 #상근
dp[4] = 1 #창영
dp[5] = 0 #상근
for i in range(6, N + 1):
    if dp[i - 1] == 1 or dp[i - 3] == 1:
        dp[i] = 0
    else :
        dp[i] = 1

print("SK" if dp[N] == 0 else "CY")