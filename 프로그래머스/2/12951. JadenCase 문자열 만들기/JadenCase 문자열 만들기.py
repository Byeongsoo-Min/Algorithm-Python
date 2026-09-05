def solution(s):
    ans = []
    isFirst = True
    for i in range(len(s)):
        if isFirst :
            isFirst = False
            if s[i].isalpha():
                ans.append(s[i].upper())
            else :
                ans.append(s[i])
        else :
            ans.append(s[i].lower())
        if s[i] == ' ':
            isFirst = True
    return ''.join(ans)