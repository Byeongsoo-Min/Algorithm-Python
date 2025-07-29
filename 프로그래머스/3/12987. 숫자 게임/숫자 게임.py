def solution(A, B):
    A.sort()
    B.sort()
    answer = 0

    i = j = 0
    n = len(A)

    while i < n and j < n:
        if B[j] > A[i]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1  # B가 이길 수 없으니 다음 B로

    return answer