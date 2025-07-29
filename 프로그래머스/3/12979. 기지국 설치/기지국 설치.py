import math

def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1  # 하나의 기지국이 커버하는 아파트 수
    start = 1             # 현재 커버되지 않은 구간의 시작

    for st in stations:
        # 현재 기지국의 커버 시작 지점
        left = max(st - w, 1)
        # left 이전 구간은 커버되지 않은 구간
        gap = left - start
        if gap > 0:
            answer += math.ceil(gap / coverage)
        # 다음 구간 시작을 이 기지국이 커버하는 범위 끝 다음으로 갱신
        start = st + w + 1

    # 마지막 기지국 뒤쪽 구간
    if start <= n:
        gap = n - start + 1
        answer += math.ceil(gap / coverage)

    return answer