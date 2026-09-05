def solution(s):
    arr = list(map(int, s.split()))
    return ' '.join([str(min(arr)), str(max(arr))])
    