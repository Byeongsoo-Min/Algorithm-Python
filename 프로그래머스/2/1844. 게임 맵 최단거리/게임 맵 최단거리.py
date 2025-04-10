from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    print(n, m)
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    visited = [[False] * (m) for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    visited[0][0] = True
    
    while q:
        x, y, dist = q.popleft()
        if (x, y) == (n - 1, m - 1) :
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    return -1