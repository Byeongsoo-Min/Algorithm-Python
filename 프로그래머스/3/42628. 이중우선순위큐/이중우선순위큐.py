def solution(operations):
    import heapq
    arr = []
    heapq.heapify(arr)
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(arr, int(i[2:]))
        if i[0] == 'D' and len(arr) != 0:
            if i[2] == "-":
                heapq.heappop(arr)
            else :
                arr.remove(max(arr))
    if len(arr) == 0 :
        return [0, 0]
    else :
        return [max(arr), arr[0]]