N = int(input())

graph = []
answer = int(1e9)
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
#print(graph)
def combinations(arr, r):
    result = []

    def dfs(start, path):
        if len(path) == r:
            result.append(path[:])  # 복사해서 저장
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i + 1, path)
            path.pop()  # 백트래킹

    dfs(0, [])
    return result    

all_kind = combinations([i for i in range(N)], N // 2)

for i in all_kind[:len(all_kind) // 2]:
    temp = 0
    temp_comp = 0
    mod_temp = [x for x in range(N)]
    for j in i:
        mod_temp.remove(j)
    for j in range(len(i)):
        for x in range(j + 1, len(i)):
            # print(f'temp i[j]: {i[j]} i[x]: {i[x]}')
            temp += graph[i[j]][i[x]]
            temp += graph[i[x]][i[j]]
    
    for j in range(len(mod_temp)):
        for x in range(j + 1, len(mod_temp)):
            # print(f'mod_temp i[j]: {i[j]} i[x]: {i[x]}')
            temp_comp += graph[mod_temp[j]][mod_temp[x]]
            temp_comp += graph[mod_temp[x]][mod_temp[j]]
    if abs(temp_comp - temp) < answer:
        # print(f'mod_temp : {mod_temp}')
        # print(f'temp: {temp} temp_comp: {temp_comp}')
        answer = abs(temp_comp - temp)

print(answer)