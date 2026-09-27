def solution(brown, yellow):
    full = brown + yellow
    for i in range(3, full + 1) :
        if (full) % i != 0 :
            continue
        if i < (full) // i :
            continue
        if (i - 2) * (full // i - 2) == yellow :
            return [i, (brown + yellow) // i]