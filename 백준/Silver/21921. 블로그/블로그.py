import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

# 초기 윈도우 합
window = sum(arr[:X])
max_sum = window
count = 1  # 최대 합이 나온 구간 수

# 슬라이딩 윈도우: 오른쪽으로 한 칸씩 이동하며 갱신 (O(1) per step)
for i in range(X, N):
    window += arr[i] - arr[i - X]
    if window > max_sum:
        max_sum = window
        count = 1
    elif window == max_sum:
        count += 1

# 출력 (모든 방문 수의 합이 0인 케이스 포함)
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)
