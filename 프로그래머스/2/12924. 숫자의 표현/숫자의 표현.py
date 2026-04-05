def solution(n):
    count = 0
    start = 1
    end = 1
    current_sum = 1
    
    while start <= n:
        if current_sum == n:
            count += 1
            current_sum -= start
            start += 1
            
        elif current_sum < n:
            end += 1
            current_sum += end
            
        else:  # current_sum > n
            current_sum -= start
            start += 1
            
    return count