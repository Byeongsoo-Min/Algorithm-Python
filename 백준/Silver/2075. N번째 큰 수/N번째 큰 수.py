import heapq

N = int(input())

ans = list(map(int, input().split()))

heapq.heapify(ans)

for _ in range(N - 1):
    for num in map(int, input().split()):
        if num > ans[0]:
            heapq.heappushpop(ans, num)

print(heapq.heappop(ans))