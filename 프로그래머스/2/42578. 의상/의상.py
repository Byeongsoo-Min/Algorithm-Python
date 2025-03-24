def solution(clothes):
    hashed_dict = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] in hashed_dict:
            hashed_dict[cloth[1]] += 1
        else:
            hashed_dict[cloth[1]] = 2
    for value in hashed_dict.values():
        answer *= value
        
    return answer - 1