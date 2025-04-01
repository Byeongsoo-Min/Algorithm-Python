def solution(number, k):
    answer = []
    max_num = -1
    num_idx = -1
    str_num = str(number)
    choose = len(number) - k
    for i in range(choose) :
        max_num = -1
        str_num = str_num[num_idx + 1:]
        length = len(str_num)
        # print(f'str_num:{str_num}, length:{length}, str_num[:length - choose + i + 1]: {str_num[:length - choose + i + 1]}')
        for idx, n in enumerate(str_num[:length - choose + i + 1]):
            if int(n) == 9:
                num_idx = idx
                max_num = int(n)
                break
            if int(n) > max_num :
                num_idx = idx
                max_num = int(n)
        answer.append(max_num)
    return ''.join(map(str,answer))
                