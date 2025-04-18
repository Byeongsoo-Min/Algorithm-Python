def solution(n, s):
    if n >= s :
        return [-1]
    divi = s // n
    mod = s % n
    
    arr = [divi] * n
    for idx in range(n - 1, 0, -1):
        if mod <= 0 :
            break
        arr[idx] += 1
        mod -= 1
    return arr
        