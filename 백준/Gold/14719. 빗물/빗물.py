H, W = map(int, input().split())

arr = list(map(int, input().split()))
length = len(arr)
ans = 0
idx = 0
while idx < length - 1:
    pr = arr[idx]
    nwIdx = idx
    find = False
    if pr != 0 :
        for jdx, nw in enumerate(arr[idx + 1:], start=idx + 1):
            if nw >= pr:
                find = True
                nwIdx = jdx
                break
    else :
        idx += 1
        continue
    if find :
        ans += (pr * (nwIdx - idx - 1)) - (sum(arr[idx + 1: nwIdx]))
        idx = nwIdx
    else :
        max_height = max(arr[idx+1:])
        max_idx = arr.index(max_height, idx+1)
        if max_idx == idx + 1:
            idx = max_idx
            continue
        ans += (max_height * (max_idx - idx - 1)) - sum(arr[idx+1:max_idx])
        idx = max_idx
print(ans)