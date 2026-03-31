def solution(n, words):
    answer = []
    used = []
    a = 0
    for idx, word in enumerate(words):
        a += 1
        if a > n :
            a = 1
        if len(used) != 0 :
            if used[-1][-1] != word[0]:
                return [a, idx // n + 1]
        if word in used:
            return [a, idx // n + 1]
        used.append(word)

    return [0, 0]