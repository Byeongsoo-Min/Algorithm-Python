def solution(begin, target, words):
    from collections import deque
    def can_convert(pv, nt):
        diff = 0
        for x, y in zip(pv, nt):
            if x != y:
                diff += 1
            if diff > 1:
                return False
        return True
    if target not in words:
        return 0
    q = deque()
    q.append((begin, 0))
    visited = set()
    while q:
        word, step = q.popleft()
        if word == target:
            return step
        for w in words:
            if w not in visited and can_convert(word, w):
                visited.add(w)
                q.append((w, step + 1))
    
        