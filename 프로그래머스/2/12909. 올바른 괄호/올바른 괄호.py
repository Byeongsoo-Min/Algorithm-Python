def solution(s):
    left = 0
    for a in s :
        if a == '(' :
            left += 1
        else :
            left -= 1
        if left < 0 :
            return False
    if left != 0 :
        return False
    return True
        