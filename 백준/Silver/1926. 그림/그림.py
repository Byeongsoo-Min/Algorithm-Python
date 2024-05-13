import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int,input().split())
canvas = []
visited = [[False] * col for _ in range(row)]

for _ in range(row):
    canvas.append(list(map(int,input().split())))
    
largest = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
amount = 0

def bfs(r, c, size):
    cv = [[r, c]]
    q = deque(cv)
    while q:
        r, c = q.popleft()
        for i in range(4):
            if 0 <= r + dx[i] < row and 0 <= c + dy[i] < col :
                if canvas[r + dx[i]][c + dy[i]] == 1 and not visited[r + dx[i]][c + dy[i]]:
                    size += 1
                    visited[r + dx[i]][c + dy[i]] = True
                    q.append((r + dx[i], c + dy[i]))
    return size
                
                
        

for i in range(row):
    for j in range(col):
        if canvas[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            amount += 1
            largest = max(largest, bfs(i, j, 1))
            
print(amount)
print(largest)