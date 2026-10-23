def solution(s):
    asd = list(map(int, s.split()))
    return str(min(asd)) + ' ' + str(max(asd))