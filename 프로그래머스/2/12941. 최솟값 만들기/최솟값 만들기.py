def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    lth = len(A)
    ans = 0
    for i in range(lth):
        ans += A[i] * B[i]
    return ans
        