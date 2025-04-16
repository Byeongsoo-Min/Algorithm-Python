def solution(arr):
    while len(arr) != 1 :
        arr.sort()
        temp = []
        for i in range(1, max(arr)):
            if arr[1] * i % arr[0] == 0:
                temp.append(arr[1] * i)
                break
        arr.remove(arr[0])
        arr.remove(arr[0])
        arr.extend(temp)
        
        
    return arr[0]