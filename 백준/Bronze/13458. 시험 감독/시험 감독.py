import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N

for i in A:
    i -= B
    if i <= 0 :
        continue
    else :
        answer += math.ceil(i / C )
print(answer)