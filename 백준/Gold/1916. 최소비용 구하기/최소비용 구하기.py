import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N = int(input())
M = int(input())

bus_table = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    bus_table[a].append((b, c))

start, end = map(int, input().split())

def dijikstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]: # 이미 최단경로 계산을 마쳤을 경우
            continue
        for i in bus_table[now]: # 그래프 돌기
            cost = dist + i[1] # 간선 비용 계산
            if cost < distance[i[0]]: # 해당 간선을 사용하는게 해당 노드로 가는 최소 비용일 경우
                distance[i[0]] = cost # 값 갱신
                heapq.heappush(q, (cost, i[0])) # 해당 간선을 사용한 방법으로 다시 진행
    return distance[end]
                
                
print(dijikstra(start, end))
    