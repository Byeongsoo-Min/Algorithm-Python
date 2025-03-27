import math
from itertools import permutations as pm
def solution(numbers):
    answer = set()
    all_kind = []
    for i in range(1, len(str(numbers)) + 1):
        all_kind.append(set(pm(str(numbers), i)))
    for i in all_kind:
        for j in i:
            j = int(''.join(j))
            if j == 1 or j == 0:
                continue
            # print(j)
            for k in range(2, int(math.sqrt(j)) + 1):
                if j % k == 0:
                    j = -1
            if j != -1:
                # print('as', j)
                answer.add(j)
        
    # print(all_kind)
    # print(len(answer))
    return len(answer)