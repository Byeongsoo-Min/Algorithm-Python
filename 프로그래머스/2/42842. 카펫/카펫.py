import math
def solution(brown, yellow):
    all_kind = []
    square = brown + yellow
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            if (i + 2) * (yellow // i + 2) == square :
                all_kind.append(i + 2) 
                all_kind.append(yellow // i + 2)
    return sorted(all_kind, reverse=True)