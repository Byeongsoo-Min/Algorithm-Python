import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-w for w in works]  # 최대 힙 구현
    heapq.heapify(works)

    for _ in range(n):
        max_work = heapq.heappop(works)
        heapq.heappush(works, max_work + 1)  # +1 because it's negative

    return sum(w ** 2 for w in works)