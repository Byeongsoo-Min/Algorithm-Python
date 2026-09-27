def solution(n):
    bin_n = list(bin(n))
    num = bin_n.count('1')
    start = n + 1
    while True :
        bin_n = list(bin(start))
        num2 = bin_n.count('1')
        if num == num2 :
            return start
        start += 1
    