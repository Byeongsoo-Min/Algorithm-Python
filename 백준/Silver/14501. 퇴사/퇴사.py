N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N):
    t, p = schedule[i]
    # 오늘 일을 하지 않는 경우
    dp[i + 1] = max(dp[i + 1], dp[i])
    # 오늘 일을 하는 경우
    if i + t <= N:
        dp[i + t] = max(dp[i + t], dp[i] + p)

print(max(dp))