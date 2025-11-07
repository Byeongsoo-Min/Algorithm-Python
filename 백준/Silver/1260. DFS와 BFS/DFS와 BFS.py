N, M, V = map(int, input().split())

arr=[[] for _ in range(N + 1) ]

for i in range(M):
   n, m = map(int, input().split())
   arr[n].append(m)
   arr[m].append(n)
   
visited = [False] * (N + 1)
dfs_print = []
def dfs(n):
    if visited[n] :
        return
    if not visited[n]:
        dfs_print.append(n)
        visited[n] = True
        temp = arr[n]
        temp.sort()
        for ar in temp:
            dfs(ar)

dfs(V)
print(*dfs_print)
        
from collections import deque
bfs = []
bfs = deque()
bfs.append(V)
bfs.extend(arr[V])
bfs_print = []
visited = [False] * (N + 1)

while bfs :
    now = bfs.popleft()
    if visited[now] :
        continue
    bfs_print.append(now)
    visited[now] = True
    temp = arr[now]
    temp.sort()
    for ar in temp:
        if not visited[ar]:
            bfs.append(ar)
            
print(*bfs_print)