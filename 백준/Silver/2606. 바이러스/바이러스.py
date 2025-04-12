from collections import deque

N = int(input())
k = int(input())
q = deque()
graph = [[] for _ in range(N)]
visited = [False] * (N)

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)
    
q.append(0)
visited[0] = True
while q:
    x = q.popleft()
    for i in graph[x]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

print(visited.count(True) - 1)
    

    
