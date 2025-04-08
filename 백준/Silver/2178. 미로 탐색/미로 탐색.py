from collections import deque

x, y = map(int, input().split())
maze = []

for _ in range(x):
    maze.append(list(input()))
    
ways = []

for idx in range(x):
    for j in range(y):
        if maze[idx][j] == '1':
            ways.append((idx, j))

visited = [[0] * y for _ in range(x)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
visited[0][0] = 1
def bfs():
    global visited
    q = deque()
    q.append((0, 0))
    while q:
        c, d = q.popleft()
        if (c, d) == (x - 1, y - 1):
            return visited[c][d]
        for qw in range(4):
            fx = c + dx[qw]
            fy = d + dy[qw]
            if 0 <= fx < x and 0 <= fy < y:
                if (fx, fy) in ways and visited[fx][fy] == 0:
                    q.append((fx, fy))
                    visited[fx][fy] = visited[c][d] + 1
 
print(bfs())
    

