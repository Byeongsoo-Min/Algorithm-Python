def solution(s):
    ans = 0
    times = 0
    t = [a for a in s]
    while True :
        if len(t) == 1 :
            break
        ans += len(t)
        t = [a for a in t if a != '0']
        ans -= len(t)
        t = bin(len(t))[2:]
        times += 1
    return [times, ans]
        
            