from itertools import permutations as pm
def solution(k, dungeons):
    answer = -1
    all_kind = []
    for i in range(1, len(dungeons) + 1):
        all_kind.append(list(pm(dungeons, i)))
        
    for i in all_kind:
        for j in i:
            now_health = k
            is_success = True
            for min_health, require in j:
                if (now_health >= min_health):
                    now_health -= require
                else :
                    is_success = False
            if is_success:
                answer = max(answer, len(j))
    return answer