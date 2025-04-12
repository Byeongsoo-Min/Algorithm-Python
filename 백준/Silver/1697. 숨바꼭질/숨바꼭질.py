from collections import deque
N, K = map(int, input().split())

visited = [False]*(100001)
time = [0] * (100001)
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        if now == K:
            return time[now]
        
        for next_pos in (now - 1, now + 1, now * 2):
            if 0 <= next_pos < 100001 and not visited[next_pos]:
                visited[next_pos] = True
                time[next_pos] = time[now] + 1
                q.append(next_pos)

print(bfs(N))
