def solution(k, tangerine):
    dict_tang = {}
    answer =0 
    for i in tangerine:
        if i not in dict_tang.keys():
            dict_tang[i] = 1
        else :
            dict_tang[i] += 1
    ranged_tang = dict(sorted(dict_tang.items(), key=lambda x:x[1], reverse=True))
    for i in ranged_tang:
        k -= ranged_tang[i]
        answer += 1
        if k <= 0 :
            return answer
        