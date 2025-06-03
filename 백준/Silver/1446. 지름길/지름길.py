N, D = map(int, input().split())
dp = [i for i in range(10001)]
dp[0] = 0
shortCut = []

for _ in range(N):
    shortCut.append(list(map(int, input().split())))
    
shortCut.sort(key=lambda x : x[0])

for i in range(0, D + 1):
    if i != 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for short in shortCut:
        if short[0] == i:
            dp[short[1]] = min(dp[short[1]], dp[i] + short[2])

print(dp[D])