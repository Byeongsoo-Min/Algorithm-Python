from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
visited = [False] * (N + 1)
visited[X] = True
arr = deque([(X, 0)])
ans = []
while arr:
    x, n = arr.popleft()
    if n > K :
        break
    if n == K:
        ans.append(x)
        continue
    for gr in graph[x]:
        if not visited[gr]:
            arr.append((gr, n + 1))
            visited[gr] = True
ans.sort()
if ans:
    sys.stdout.write('\n'.join(map(str, sorted(ans))))
else:
    sys.stdout.write('-1\n')