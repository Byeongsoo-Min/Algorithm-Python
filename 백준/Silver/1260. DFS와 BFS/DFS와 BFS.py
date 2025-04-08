N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i].sort()
    

visited = [False] * (N + 1)

def dfs(v):
    global visited
    visited[v] = True
    print(v, end=" ")
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        a = q.pop(0)
        print(a, end=" ")
        for next in range(1, N + 1):
            if not visited[next] and next in graph[a]:
                visited[next] = True
                q.append(next)
dfs(V)
print()
q = [V]
visited = [False] * (N + 1)
visited[V] = True    
bfs()