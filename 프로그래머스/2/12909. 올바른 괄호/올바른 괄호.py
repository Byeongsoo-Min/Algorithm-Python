def solution(s):
    answer = True
    left = 0
    right = 0
    for c in list(s):
        if c == "(":
            left += 1
        else :
            right += 1
            if right > left:
                return False
    if right != left:
        return False
    return True