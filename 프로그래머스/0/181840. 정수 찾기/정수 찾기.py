def solution(num_list, n):
    answer = 0
    try :
        return 1 if num_list.index(n) else 0
    except :
        return 0
    # a = num_list.index(n)
    # return 1 if num_list.index()