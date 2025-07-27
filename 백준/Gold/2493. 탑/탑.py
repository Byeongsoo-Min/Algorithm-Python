N = int(input())
dp = [0] * (N + 1)
li = list(map(int, input().split()))
li.insert(0, 0)
for idx in range(2, N + 1):
    if li[idx] <= li[idx - 1]:
        dp[idx] = idx - 1
    else :
            sch = idx - 1
            while True:
                if li[dp[sch]] < li[idx]:
                    sch = dp[sch]
                    if sch == 0:
                        break
                else :
                    dp[idx] = dp[sch]
                    break
print(*dp[1:])