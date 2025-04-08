def solution(n, computers):
    visited = [False] * (n)
    networks = [[] for _ in range(n)]
    
    def dfs(idx):
        nonlocal visited
        visited[idx] = True
        for i in range(n):
            if not visited[i] and computers[idx][i] == 1 and idx != i:
                networks[idx].append(i)
                dfs(i)
    answer = n
    idx = 0
    while not all(visited) :
        dfs(idx)
        idx += 1
    # print(visited)
    # print(networks)
    for i in networks:
        answer -= len(i) 
    return answer
    