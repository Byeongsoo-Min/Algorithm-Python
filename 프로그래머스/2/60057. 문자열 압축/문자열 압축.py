def solution(s):
    length = len(s)
    result = ["a"*1001]*(length//2 + 1)
    mini = 1001
    if length == 1:
        return 1
    for i in range(1, length//2 + 1):
        prev = s[0:i]
        n = 0
        result[i] = ""
        for x in range(0, length, i):
            if prev == s[x:x + i]:
                n += 1
            else:
                if n != 1:
                    result[i] += f"{n}{prev}"
                    n = 1
                    prev = s[x:x + i]
                else :
                    result[i] += prev
                    n = 1
                    prev = s[x:x + i]
        if n != 1:
            result[i] += f"{n}{prev}"
        else:
            result[i] += prev
                    
        
    for i in result:
        mini = min(mini, len(i))
    return mini