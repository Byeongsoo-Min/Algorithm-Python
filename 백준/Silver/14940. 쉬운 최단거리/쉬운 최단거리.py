from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n)]

q = deque()
visited = [[False] * m for i in range(n)]

for x in range(n):
    for y in range(m):
        if graph[x][y] == 2 :
          q.append((x, y, 0))
          visited[x][y] = True
          break

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

new_graph = [[0] * m for _ in range(n)]

while q:
    x, y, cnt = q.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= (new_x) < n and 0 <= (new_y) < m :
            if not visited[new_x][new_y] and graph[new_x][new_y] != 0:
                visited[new_x][new_y] = True
                new_graph[new_x][new_y] = cnt + 1
                q.append((new_x, new_y, cnt + 1))


for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] != 0:
            new_graph[x][y] = -1

for i in new_graph:
    print(*i)
                