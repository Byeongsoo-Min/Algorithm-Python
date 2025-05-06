from collections import deque

S = input()
T = input()

ace = T.count('A')
bug = T.count('B')
q = deque()
q.append((S, S.count('A'), S.count('B')))
find = False

def dfs(current):
    if current == S:
        return True
    if len(current) < len(S):
        return False

    result = False
    if current[-1] == 'A':
        result |= dfs(current[:-1])
    if current[0] == 'B':
        result |= dfs(current[1:][::-1])
    return result

if dfs(T):
    print(1)
else:
    print(0)
    