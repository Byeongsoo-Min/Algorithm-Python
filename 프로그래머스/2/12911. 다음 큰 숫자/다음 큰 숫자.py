def solution(n):
    bin_n = str(bin(n))[2:]
    cnt = 0
    find = False
    for i in bin_n:
        if i == "1":
            cnt += 1
    while not find:
        n += 1
        bigNum = str(bin(n))[2:]
        cnt_big = 0
        for i in bigNum:
            if i == "1":
                cnt_big += 1
        if cnt == cnt_big:
            return n