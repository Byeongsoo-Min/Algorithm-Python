N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N - 1
ans = abs(arr[left] + arr[right])
ans_pair = (arr[left], arr[right])

while left < right:
    temp = arr[left] + arr[right]

    if abs(temp) < ans:
        ans = abs(temp)
        ans_pair = (arr[left], arr[right])

    if temp < 0:   # 합이 음수 → 값을 키워야 0에 가까워짐
        left += 1
    elif temp > 0: # 합이 양수 → 값을 줄여야 0에 가까워짐
        right -= 1
    else:          # temp == 0 → 0이 가장 가까움
        break

print(ans_pair[0], ans_pair[1])