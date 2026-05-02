from collections import Counter

def solution(topping):
    answer = 0
    
    # 1. 처음엔 오른쪽 조각이 모든 토핑을 다 가진다고 가정 (딕셔너리 형태)
    right_topping = Counter(topping)
    
    # 2. 왼쪽 조각이 가질 토핑의 종류를 담을 세트 (초기엔 비어있음)
    left_topping = set()
    
    # 3. 토핑을 순회하며 하나씩 왼쪽으로 옮기기
    for t in topping:
        # 왼쪽 조각에 토핑 종류 추가
        left_topping.add(t)
        
        # 오른쪽 조각에서는 해당 토핑 개수 1 감소
        right_topping[t] -= 1
        
        # 오른쪽 조각에서 해당 토핑이 0개가 되면 종류에서 완전히 제거 (키 삭제)
        if right_topping[t] == 0:
            del right_topping[t]
            
        # 양쪽의 토핑 종류 개수가 같으면 정답 +1
        if len(left_topping) == len(right_topping):
            answer += 1
            
    return answer