def solution(triangle):
    dp_triangle = [[0] * i for i in range(1, len(triangle) + 1)]
    
    dp_triangle[0][0] = triangle[0][0]
    # print(dp_triangle)
    dx = [-1, -1]
    dy = [0, -1]
    n = len(triangle)
    for i in range(1, n):
        for j in range(len(triangle[i])):
            # print(len(triangle[i]))
            for k in range(2):
                if i + dx[k] >= 0 and j + dy[k] >= 0 and j + dy[k] < len(triangle[i - 1]):
                    previous_x = i + dx[k]
                    previous_y = j + dy[k]
                    # print("previous_x: ", previous_x)
                    # print("previous_y: ", previous_y)
                    now = dp_triangle[previous_x][previous_y] + triangle[i][j]
                    # print(now)
                    if dp_triangle[i][j] <= now:
                        dp_triangle[i][j] = now
                        
    return max(dp_triangle[n - 1])