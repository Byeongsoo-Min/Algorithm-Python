from collections import Counter
T = int(input())
wList = []
kList = []
for _ in range(T):
    wList.append(input())
    kList.append(int(input()))


for t in range(T):
    W = wList[t]
    K = kList[t]
    S = Counter(W)
    shortOut = 10001
    longOut = 0
    if S.most_common(1)[0][1] < K:
        print(-1)
        continue
    for s in S.keys():
        if S[s] >= K:
            idxList = []
            short = 10001
            long = 0
            for idx, w in enumerate(W):
                if w == s:
                    idxList.append(idx)
            for i in range(S[s] - K + 1):
                short = min(short, idxList[i + K - 1] - idxList[i] + 1)
                long = max(long, idxList[i + K - 1] - idxList[i] + 1)
            shortOut = min(shortOut, short)
            longOut = max(longOut, long)
    print(shortOut, longOut)