import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
out = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            out.append(str(heapq.heappop(heap)))
        else:
            out.append('0')
    else:
        heapq.heappush(heap, x)

sys.stdout.write("\n".join(out))
