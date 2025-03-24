from collections import deque

def solution(progresses, speeds):
    days = 0
    functions = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        days += 1
        count = 0
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count > 0:
            functions.append(count) 
    
    return functions