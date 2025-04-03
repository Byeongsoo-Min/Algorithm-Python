def solution(s):
    answer = []
    cnt = 0
    idx = 0
    while s != "1": 
        temp = []
        idx += 1
        for i in s:
            if i == '1':
                temp.append(i)
            else :
                cnt += 1
        s = str(bin(len(temp)))[2:]
    answer.append(idx)
    answer.append(cnt)
    return answer