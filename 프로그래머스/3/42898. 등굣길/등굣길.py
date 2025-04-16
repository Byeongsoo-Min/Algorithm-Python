def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    MOD = 10**9 + 7
    puddles = set((y, x) for x, y in puddles)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) in puddles:
                dp[i][j] = 0
            elif i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]