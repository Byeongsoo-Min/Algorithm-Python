from collections import deque
N, M = map(int, input().split())
cities = []
chickens = []
houses = []
dist_table = []
cities.append([0]*(N+1))

for _ in range(N):
    city = list(map(int, input().split()))
    city.insert(0, 0)
    cities.append(city)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cities[i][j] == 1:
            houses.append((i, j))
        elif cities[i][j] == 2:
            chickens.append((i, j))
def combinations(arr, n):
    array = []
    
    def dfs(idx, path):
        if len(path) == n:
            array.append(path[:])
            return
        for i in range(idx, len(arr)):
            path.append(arr[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return array

def find_short(x, y, temp_chickens):
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    visited[x][y] = True
    q = deque()
    q.append((x, y, 0))
    while q :
        cx, cy, distance = q.popleft()
        if (cx, cy) in temp_chickens:
            return distance
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 1<= nx <= N and 1 <= ny <= N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, distance + 1))
    return -1
                    
            
                
comb = combinations(chickens, M)
all_chicken_distance = int(1e9)
dist_table = [[abs(hx - cx) + abs(hy - cy) for (cx, cy) in chickens] for (hx, hy) in houses]
for chicken in comb:
    temp = 0
    for i in range(len(houses)):
        temp += min([dist_table[i][chickens.index(c)] for c in chicken])
    all_chicken_distance = min(all_chicken_distance, temp)
print(all_chicken_distance)