N, K = map(int, input().split())

numArray = list(map(int, input().split()))

start = 0
end = 0
counter = [0] * 100001
counter[numArray[0]] += 1
max_len = 0

for n in range(1, N):
    end += 1
    counter[numArray[end]] += 1
    if counter[numArray[n]] > K :
        for i in range(start, end):
            counter[numArray[i]] -= 1
            if numArray[i] == numArray[n] :
                start = i + 1
                break
    max_len = max(max_len, end - start + 1)

print(max_len)