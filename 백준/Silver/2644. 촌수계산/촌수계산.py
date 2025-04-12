from collections import deque

n = int(input())

me, you = map(int, input().split())

k = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
result = []

def dfs(x, count):
    global flag
    visited[x] = True
    if x==you:
        flag=True
        print(count)
        return
    for val in graph[x]:
        if visited[val] == False:
            dfs(val,count+1)

flag=False
dfs(me,0)
if flag==False:
    print(-1)