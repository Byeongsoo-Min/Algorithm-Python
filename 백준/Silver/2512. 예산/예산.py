N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()
dp = [0] * N
if sum(arr) > M :
    low = 1
    avg = M // N 
    high = M
    ans = 0
    while low <= avg <= high :
        cnt = 0
        jdx = 0
        for idx in range(N):
            if arr[idx] >= avg :
                cnt += avg * (N - idx)
                jdx = idx
                break
            else :
                cnt += arr[idx]
        if cnt < M :
            if M - cnt < N - jdx :
                print(avg)
                break
            low = avg + 1
            avg = (avg + high) // 2
        elif cnt > M :
            high = avg - 1
            avg = (avg + low) // 2
        else :
            print(avg)
            break
else :
    print(arr[-1])