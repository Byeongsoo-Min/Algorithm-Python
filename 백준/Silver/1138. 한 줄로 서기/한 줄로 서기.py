N = int(input())

orders = list(map(int, input().split()))

ans = [0] * (N)
visited = [False] * (N + 1)
# 1번째 사람

for idx, order in enumerate(orders):
    start = 0
    while True :
        if order == 0 :
            while visited[start] :
                start += 1
            visited[start] = True
            ans[start] = idx + 1
            break
        if not visited[start] :
            order -= 1
        start += 1

print(*ans)
        