def solution(s):
    stack = []
    for char in s:
        # print(stack)
        if stack and stack[-1] == char:
            stack.pop()  # 짝이 맞으면 제거
        else:
            stack.append(char)  # 짝이 안 맞으면 추가

    return 1 if not stack else 0