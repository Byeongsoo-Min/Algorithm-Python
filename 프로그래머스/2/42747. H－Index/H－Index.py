def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    answer = 0
    for i in range(len(citations)):
        if (i + 1 > citations[i]):
            answer = i
            return answer
    return len(citations)