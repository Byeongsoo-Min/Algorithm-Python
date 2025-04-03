def solution(k, tangerine):
    cnt_dict = {}
    for i in tangerine:
        if i in cnt_dict :
            cnt_dict[i] += 1
        else :
            cnt_dict[i] = 1
    sorted_array = []
    sorted_array = sorted(cnt_dict.values(), reverse=True)
    for idx, value in enumerate(sorted_array):
        k -= value
        if k <= 0 :
            return idx + 1
        
    # return answer