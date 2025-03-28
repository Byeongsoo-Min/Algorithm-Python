from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt
def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        start = 0
        tmps.pop(i)
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx, gr in enumerate(graph):
            if gr != []:
                start = idx
                break
        cnts = bfs(graph, start, visited)
        others_cnts = n - cnts
        if answer > abs(cnts - others_cnts):
            answer = abs(cnts - others_cnts)
    return answer