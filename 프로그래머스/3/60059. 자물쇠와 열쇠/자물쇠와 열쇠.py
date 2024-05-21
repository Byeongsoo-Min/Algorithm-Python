def rotate(key):
    n = len(key)
    result = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = key[i][j]
    return result

def check(lock):
    lock_length = len(lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)
    zero_lock = [[0]*(lock_length*3) for _ in range(lock_length * 3)]
    for i in range(lock_length):
        for j in range(lock_length):
            zero_lock[i + lock_length][j + lock_length] = lock[i][j]
    for _ in range(4):
        key = rotate(key)
        for x in range(1,lock_length*2):
            for y in range(1,lock_length*2):
                for i in range(key_length):
                    for j in range(key_length):
                        zero_lock[x+i][y+j] += key[i][j]
                if check(zero_lock) == True:
                    return True
                for i in range(key_length):
                    for j in range(key_length):
                        zero_lock[x+i][y+j] -= key[i][j]
    return False