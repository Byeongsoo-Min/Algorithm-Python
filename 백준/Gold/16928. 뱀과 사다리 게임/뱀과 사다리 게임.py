from collections import deque

N, M = map(int, input().split())
ladders = {}
snakes = {}
dp = [1e9] * 101

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(M):
    x, y = map(int , input().split())
    snakes[x] = y
    
q = deque()

visited = [False] * 101
visited[1] = True
q.append((1, 0))
dp[1] = 0
while q:
    cur, time = q.popleft()
    if cur == 100:
        break
    for i in range(1, 7):
        next_pos = cur + i
        if next_pos > 100:
            continue
        if next_pos in ladders:
            next_pos = ladders[next_pos]
        elif next_pos in snakes:
            next_pos = snakes[next_pos]
        if not visited[next_pos]:
            visited[next_pos] = True
            dp[next_pos] = time + 1
            q.append((next_pos, time + 1))
            
print(dp[100])