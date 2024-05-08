import sys
from collections import deque

lineInput = sys.stdin.readline

M, N, H = map(int, lineInput().split())

tomatoes = []
rottenTomatoes = []

for h in range(H):
    tomato = []
    for n in range(N):
        tomato.append(list(map(int, lineInput().split())))
    tomatoes.append(tomato)
    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 1:
                rottenTomatoes.append((h, n, m, 0))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
days = 0

rottenTomatoes = deque(rottenTomatoes)

def rotten():
    global tomatoes, days
    
    while rottenTomatoes:
        z, y, x, d = rottenTomatoes.popleft()
        for i in range(6):
            if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N and 0 <= z + dz[i] < H :
                if tomatoes[z + dz[i]][y + dy[i]][x + dx[i]] == 0 :
                    tomatoes[z + dz[i]][y + dy[i]][x + dx[i]] = 1
                    rottenTomatoes.append((z + dz[i], y + dy[i], x + dx[i], d + 1))
            
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 0 :
                    return -1
    return d
            
print(rotten())
    