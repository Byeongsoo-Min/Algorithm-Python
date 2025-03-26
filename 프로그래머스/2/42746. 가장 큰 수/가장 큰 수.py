def solution(numbers):
    # str_num = list(map(str, numbers))
    if sum(numbers) == 0:
        return '0'
    numbers.sort(reverse= True,key = lambda x : (str(x)*3, -len(str(x)), x))
    return(''.join(map(str, numbers)))