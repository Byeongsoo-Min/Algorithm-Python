from heapq import *
def solution(scoville, K):
    heapify(scoville)
    scoville_hot = False
    count = 0
    while not scoville_hot:
        least = heappop(scoville)
        if least >= K:
            scoville_hot = True
            break
        minor = heappop(scoville)
        new_scoville = least + minor * 2
        heappush(scoville, new_scoville)
        count += 1
        
        if len(scoville) == 1:
            if new_scoville >= K:
                scoville_hot = True
            break
    if scoville_hot :
        return count
    else:
        return -1