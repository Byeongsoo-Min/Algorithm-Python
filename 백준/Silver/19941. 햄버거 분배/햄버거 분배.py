N, K = map(int, input().split())

arr = input()
length = len(arr)
mir_arr = [0] * length
ans = 0

for idx in range(length):
    if arr[idx] == 'P':
        for jdx in range(max(0, idx - K), min(length, idx + K + 1)):
            if arr[jdx] == 'H' and mir_arr[jdx] == 0:
                mir_arr[jdx] = 1
                mir_arr[idx] = 1
                ans += 1
                break
    else :
        continue

print(ans)
    