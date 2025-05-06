from collections import deque

N, K = map(int, input().split())
MAX = 100001
dist = [1e9] * MAX
dist[N] = 0

dq = deque()
dq.append(N)

while dq:
    cur = dq.popleft()

    if cur == K:
        print(int(dist[K]))
        break

    # 순간이동: 시간 그대로
    if 0 <= cur * 2 < MAX and dist[cur * 2] > dist[cur]:
        dist[cur * 2] = dist[cur]
        dq.appendleft(cur * 2)

    # 걷기: 시간 +1
    if 0 <= cur - 1 < MAX and dist[cur - 1] > dist[cur] + 1:
        dist[cur - 1] = dist[cur] + 1
        dq.append(cur - 1)

    if 0 <= cur + 1 < MAX and dist[cur + 1] > dist[cur] + 1:
        dist[cur + 1] = dist[cur] + 1
        dq.append(cur + 1)