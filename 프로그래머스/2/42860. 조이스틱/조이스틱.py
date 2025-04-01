def solution(name):
    answer = 0
    a_idx = ord("A")
    z_idx = ord("Z")
    a_array = []
    def make_alpha(alpha):
        import math
        return min(abs(ord(alpha) - a_idx), abs(z_idx - ord(alpha)) + 1)
    for i in range(len(name)):
        answer += make_alpha(name[i])
        a_array.append(name[0:i + 1].count("A"))
    move = len(name) - 1
    for i in range(len(name)):
        next_idx = i + 1  
        while next_idx < len(name) and name[next_idx] == "A":  # 연속된 'A' 찾기
            next_idx += 1
        
        # 이동 거리 = 현재 위치(i)까지 왔다가 되돌아간 후, A 블록 건너뛰기
        move = min(move, i + i + (len(name) - next_idx), (len(name) - next_idx) * 2 + i)
    return answer + move