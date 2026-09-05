def solution(n):
    ans = 1
    for i in range(2, n):
        if ((n - sum(range(i))) / i) <= 0 :
            break
        if ((n - sum(range(i))) / i).is_integer():
            ans += 1
    return ans
    